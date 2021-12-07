<template>
  <section>
    <v-navigation-drawer
      color="#0F3357"
      dark
      permanent
      clipped
      app
      width="13%"
      :style="{ top: $vuetify.application.top + 'px', zIndex: 4 }"
    >
      <v-list dense nav>
        <v-list-item><strong>Select a Dashboard</strong> </v-list-item>
        <v-list-item v-for="item in items" :key="item.tab" link :to="item.to">
          <v-list-item-content>
            <v-list-item-title>{{ item.tab }}</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>

    <v-card class="ma-5 align-center" color="#21ACBF" dark>
      <v-card-title class="">
        <div class="">
          <span class="section-header"> Dashboard </span>
        </div>

        <v-spacer></v-spacer>
      </v-card-title>
      <v-card-text class="section-description px-5" align="justify">
        Get instant social intelligence tailored to your specific digital needs.
        By addressing the challenge most organizations have on resources and
        staff the interactive dashboard is a flexible tool for customization
        providing key trends, narratives and influencers on Twitter. Once you
        select a dashboard, you can use the custom filters based on the curated
        source panels, combined with a specific search and topics and, lastly,
        define a period of time to narrow down your results.
      </v-card-text>
    </v-card>

    <v-card class="ma-5 d-flex align-center">
      <v-text-field class="mx-5" label="Search" v-model="search"></v-text-field>
      <v-autocomplete
        clearable
        class="mx-5"
        label="Topic"
        v-model="topic_select.select"
        :items="topic_select.items"
      ></v-autocomplete>
      <v-dialog v-model="dialog" persistent max-width="600px">
        <template v-slot:activator="{ on, attrs }">
          <v-btn color="#0F3357" class="mr-5" dark v-bind="attrs" v-on="on">
            More Filters
          </v-btn>
        </template>
        <v-card>
          <v-card-title>
            <span class="text-h5">Financial Institution Filters</span>
          </v-card-title>
          <v-card-text>
            <v-container>
              <v-row>
                <v-col
                  cols="12"
                  sm="6"
                  v-for="filter in filters"
                  :key="filter.name"
                >
                  <v-autocomplete
                    clearable
                    :items="filter.items"
                    :label="filter.name"
                    v-model="filter.select"
                  ></v-autocomplete>
                </v-col>
              </v-row>
            </v-container>
          </v-card-text>
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn color="blue darken-1" text @click="dialog = false">
              Close
            </v-btn>
            <v-btn color="blue darken-1" text @click="dialog = false">
              Filter
            </v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>
      <v-divider class="ma-2" vertical></v-divider>

 <vue-datepicker-local v-model="range" :local="local" ></vue-datepicker-local>

      <v-btn class="mx-5" text color="#0F3357" @click="getStatus()">
        HIT
      </v-btn>
    </v-card>

    <div class="text-center" v-if="active_filters.active">
      <v-chip
        class="ma-0"
        color="transparent"
        style="font-size: 20px"
        label
        text-color="black"
      >
        <v-icon size="20" left> mdi-filter </v-icon>
        Active Filters:
      </v-chip>
    
      <span v-for="active_filter in Object.keys(active_filters.filters)"
        :key="active_filter.type">
      <v-chip v-if="active_filters.filters[active_filter].value != '' && active_filters.filters[active_filter].value != None"

        class="ma-2"
        color="cyan"
        label
        text-color="white"
      >
        <v-icon left> mdi-twitter </v-icon>
        {{ active_filter }}: {{ active_filters.filters[active_filter].value }}
      </v-chip>
      </span>

    </div>

    <stats-card :statisticsData="statisticsData"> </stats-card>

    <v-card id="wrapper" class="ma-10">
      <div id="chart-area">
        <apexchart
          type="area"
          height="300"
          :options="timeline2.chartOptionsArea"
          :series="[{ data: chart_data }]"
        ></apexchart>
      </div>
    </v-card>
    <v-col class="" cols="12">
      <v-card class="ma-6">
        <div id="topic_result_chart">
          <apexchart
            ref="realtimeChartTopicResult"
            type="bar"
            height="350"
            :options="topic_result.chartOptions"
            :series="topic_result.series"
          ></apexchart>
        </div>
      </v-card>
    </v-col>
    <v-row class="ma-6">
      <v-col cols="6">
        <v-card>
          <div id="user_mention_chart">
            <apexchart
              ref="realtimeChartUserMention"
              type="bar"
              height="350"
              :options="user_mentions.chartOptions"
              :series="user_mentions.series"
            ></apexchart>
          </div>
        </v-card>
      </v-col>
      <v-col cols="6">
        <v-card>
          <div id="screen_names_chart">
            <apexchart
              ref="realtimeChartScreenNames"
              type="bar"
              height="350"
              :options="screen_names.chartOptions"
              :series="screen_names.series"
            ></apexchart>
          </div>
        </v-card>
      </v-col>

      <v-col class="ma-0" cols="6">
        <v-sheet rounded elevation="3">
          <h1 class="ma-8 pt-5">Top Hashtags</h1>
          <v-data-table
            :headers="hashtags.headers"
            :items="hashtags.data"
            :items-per-page="10"
            class="elevation-1 ma-5"
          ></v-data-table>
          <br />
        </v-sheet>
      </v-col>

      <v-col class="ma-0" cols="6">
        <v-sheet rounded elevation="3">
          <h1 class="ma-8 pt-5">Top Links</h1>
          <v-data-table
            :headers="urls.headers"
            :items="urls.data"
            :items-per-page="10"
            class="elevation-1 ma-5"
          ></v-data-table>
          <br />
        </v-sheet>
      </v-col>

      <v-sheet class="ma-8" rounded elevation="3">
        <h1 class="ma-8 pt-5">Top Hashtags</h1>
        <v-data-table
          :headers="statusTable.headers"
          :items="statusTable.data"
          :items-per-page="10"
          class="elevation-1 ma-5"
        ></v-data-table>
        <br />
      </v-sheet>
    </v-row>

    <masonry class="ma-5" :cols="{ default: 3, 1000: 2, 700: 2, 400: 1 }">
      <div class="my-2 mx-0" v-bind:key="item._id" v-for="item in status">
        <TwitterCard :item="item"></TwitterCard>
      </div>
    </masonry>
  </section>
</template>

<script>
import axios from "axios";
import TwitterCard from "../components/TwitterCard.vue";
import VueApexCharts from "vue-apexcharts";
import StatsCard from "../components/StatsCard.vue";
import VueDatepickerLocal from 'vue-datepicker-local'

export default {
  name: "Dashboard",

  data() {
    return {
         range: [new Date(2020,0,1),new Date(2021,0,1)],
            emptyTime: '',
            emptyRange: [],
            local: {
              dow: 0, // Sunday is the first day of the week
              hourTip: 'Select Hour', // tip of select hour
              minuteTip: 'Select Minute', // tip of select minute
              secondTip: 'Select Second', // tip of select second
              yearSuffix: '', // suffix of head year
              monthsHead: 'January_February_March_April_May_June_July_August_September_October_November_December'.split('_'), // months of head
              months: 'Jan_Feb_Mar_Apr_May_Jun_Jul_Aug_Sep_Oct_Nov_Dec'.split('_'), // months of panel
              weeks: 'Su_Mo_Tu_We_Th_Fr_Sa'.split('_'), // weeks,
              cancelTip: 'cancel',
              submitTip: 'confirm'
            },
      timeline2: {
        seriesArea: [
          {
            data: this.chart_data,
          },
        ],
        chartOptionsArea: {
          title: {
            text: "Tweets Volume Evolution",
            style: {
              fontSize: "24px",
              fontWeight: "bold",
              fontFamily: "Merriweather",
              color: "#263238",
            },
          },
          chart: {
            id: "yt",
            group: "social",
            type: "area",
            height: 300,
          },
          xaxis: {
            type: "datetime",
          },
          colors: ["#00E396"],
          yaxis: {
            labels: {
              minWidth: 40,
            },
          },
        },
      },

      statisticsData: [
        {
          title: "Tweets",
          total: "---",
          icon: "mdi-twitter",
        },
        {
          title: "Financial Institutions",
          total: "---",
          icon: "mdi-briefcase",
        },
        // {
        //   title: "Engagement",
        //   total: "250k",
        //   icon: "mdi-share-variant-outline",
        // },
        {
          title: "Hashtags",
          total: "---",
          icon: "mdi-pound-box-outline",
        },
        {
          title: "User Mentions",
          total: "---",
          icon: "mdi-account-arrow-right",
        },
        {
          title: "Links",
          total: "---",
          icon: "mdi-link",
        },
      ],
      user_mentions: {
        series: [
          {
            data: [],
          },
        ],
        chartOptions: {
          title: {
            text: "Top Mentioned Profiles",
            style: {
              fontSize: "24px",
              fontWeight: "bold",
              fontFamily: "Merriweather",
              color: "#263238",
            },
          },
          chart: {
            type: "bar",
            height: 350,
          },
          plotOptions: {
            bar: {
              borderRadius: 4,
              horizontal: true,
            },
          },
          dataLabels: {
            enabled: false,
          },
          xaxis: {
            categories: [],
          },
        },
      },
      screen_names: {
        series: [
          {
            data: [],
          },
        ],
        chartOptions: {
          title: {
            text: "Top Twitters Profiles",
            style: {
              fontSize: "24px",
              fontWeight: "bold",
              fontFamily: "Merriweather",
              color: "#263238",
            },
          },
          chart: {
            type: "bar",
            height: 350,
          },
          plotOptions: {
            bar: {
              borderRadius: 4,
              horizontal: true,
            },
          },
          dataLabels: {
            enabled: false,
          },
          xaxis: {
            categories: [],
          },
        },
      },
      topic_result: {
        series: [
          {
            data: [],
          },
        ],
        chartOptions: {
          title: {
            text: "Topic Distribution",
            style: {
              fontSize: "24px",
              fontWeight: "bold",
              fontFamily: "Merriweather",
              color: "#263238",
            },
          },
          chart: {
            height: 350,
            type: "bar",
          },
          plotOptions: {
            bar: {
              borderRadius: 10,
              dataLabels: {
                position: "top", // top, center, bottom
              },
            },
          },
          dataLabels: {
            enabled: true,
            formatter: function (val) {
              return val + "%";
            },
            offsetY: -20,
            style: {
              fontSize: "12px",
              colors: ["#304758"],
            },
          },
          xaxis: {
            categories: [],
          },
        },
      },
      status: [],
      urls:{
          headers:[ 
              { text: "Link", value: "key" },
              { text: "Count", value: "doc_count" },
          ],
          data:[]
      },
      statusTable: {
        headers: [
          { text: "Date", value: "created_at" },
          { text: "User", value: "user.screen_name" },
          { text: "Tweet", value: "content" },
          { text: "Retweets", value: "retweet_count" },
          { text: "Likes", value: "favorite_count" },
        ],
        data: [],
      },
      search: "",
      dates: ["2021-01-01", "2021-08-31"],
      menu: false,
      dialog: false,
      chart_data: [],
      items: [
        { tab: "Companies", to: "/dashboard" },
        { tab: "Financial Institutions", to: "/financial" },
        { tab: "Journalists", to: "/journalist" },
      ],
      filters: [
        { name: "Name",field:"financial_name",select:"" },
        { name: "Financial Type",field:"financial_type",select:"" },
        { name: "Headquarters",field:"financial_headquarters",select:"" },
        { name: "Commodities",field:"financial_commodity",select:"" },
        { name: "Sustainability commitments",field:"financial_signatories",select:"" },
      ],
      topic_select: {
        select: '',
        items: [""],
      },
      active_filters: {
        active: true,
        filters: {},
      },
      hashtags: {
        headers: [
          { text: "Hashtag", value: "key" },
          { text: "Count", value: "doc_count" },
        ],
        data: [],
      },
    };
  },
  mounted() {
    this.setDate(365);
    this.getStatus();
  },
  methods: {
    updateSearch() {
      this.active_filters.filters.search = {
        value: this.search,
        destructor: () => {
          this.search = "";
          delete this.active_filters.filters.search;
        },
      };
      if (this.active_filters.filters.search == "") {
        delete this.active_filters.filters.search;
      }
    },
    updateTopic() {

    },
    getStatus() {
      this.activeFilters;
      var filters_url = "";
      for (var filter of this.filters) {
        filters_url = `${filters_url}&facet=${filter.field}&${filter.field}=${
          filter.select == null ? "" : filter.select
        }`;
      }
        this.topic_select.select = this.topic_select.select.toLowerCase()

      var allTopics =
        "monitoring__nature__climate__risks__deforestation__certification__esg__landuse__sourcing__protocol__paper__beef__agenda__social__soy__fires__commodities__palm";
      var url_query = `/search/status/?facet=topic_result&topic__in=${
        this.topic_select.select == '' ? allTopics : this.topic_select.select
      }&facet=topic_set&facet=financial_cnt&facet=hashtags&facet=screen_names&facet=user_mentions&facet=urls&list=financial&created_at__gte=${
         this.dateFormat(this.range[0])
      }&created_at__lte=${this.dateFormat(this.range[1])}&facet=created_at${filters_url}`;
      if (this.search != null && this.search != "")
        url_query = url_query + `&search=${this.search}`;
      axios.get(url_query).then((res) => {
        this.hashtags.data = res.data.facets._filter_hashtags.hashtags.buckets;
        this.urls.data = res.data.facets._filter_urls.urls.buckets;

        this.status = res.data.results.slice(0, 12);
        this.statusTable.data = res.data.results;
        this.statisticsData[0].total =
          res.data.facets._filter_financial_cnt.doc_count;
        this.statisticsData[1].total =
          res.data.facets._filter_financial_cnt.financial_cnt.buckets.length;
        this.statisticsData[2].total =
          res.data.facets._filter_hashtags.hashtags.buckets.reduce(
            (n, { doc_count }) => n + doc_count,
            res.data.facets._filter_hashtags.hashtags.sum_other_doc_count
          );
        this.statisticsData[3].total =
          res.data.facets._filter_user_mentions.user_mentions.buckets.reduce(
            (n, { doc_count }) => n + doc_count,
            res.data.facets._filter_hashtags.hashtags.sum_other_doc_count
          );
        this.statisticsData[4].total =
          res.data.facets._filter_urls.urls.buckets.reduce(
            (n, { doc_count }) => n + doc_count,
            res.data.facets._filter_hashtags.hashtags.sum_other_doc_count
          );
        this.chart_data =
          res.data.facets._filter_created_at.created_at.buckets.map((x) => [
            x.key,
            x.doc_count,
          ]);
        this.user_mentions.chartOptions.xaxis.categories =
          res.data.facets._filter_user_mentions.user_mentions.buckets
            .map((x) => x.key)
            .slice(0, 10);

        this.user_mentions.series[0].data =
          res.data.facets._filter_user_mentions.user_mentions.buckets
            .map((x) => x.doc_count)
            .slice(0, 10);
        this.screen_names.series[0].data =
          res.data.facets._filter_screen_names.screen_names.buckets.map(
            (x) => x.doc_count
          );
        this.screen_names.chartOptions.xaxis.categories =
          res.data.facets._filter_screen_names.screen_names.buckets.map(
            (x) => x.key
          );
        this.topic_result.series[0].data =
          res.data.facets._filter_topic_result.topic_result.buckets.map((x) =>
            (
              (x.doc_count / res.data.facets._filter_topic_result.doc_count) *
              100
            ).toFixed(2)
          );

        this.topic_result.chartOptions.xaxis.categories =
          res.data.facets._filter_topic_result.topic_result.buckets.map(
            (x) => x.key
          );

        this.topic_select.items =
          res.data.facets._filter_topic_set.topic_set.buckets.map((x) => x.key);
         this.filters[0].items = 
          res.data.facets._filter_financial_name.financial_name.buckets.map(
            (x) => x.key
        );
        this.filters[1].items = 
          res.data.facets._filter_financial_type.financial_type.buckets.map(
            (x) => x.key
        );
        this.filters[2].items = 
          res.data.facets._filter_financial_headquarters.financial_headquarters.buckets.map(
            (x) => x.key
        );
        this.filters[3].items = 
          res.data.facets._filter_financial_commodity.financial_commodity.buckets.map(
            (x) => x.key
        );
        this.filters[4].items = 
          res.data.facets._filter_financial_signatories.financial_signatories.buckets.map(
            (x) => x.key
        );
        this.updateSeriesLine();
        this.topic_select.items = this.topic_select.items.map(x => x.charAt(0).toUpperCase() + x.slice(1))
      });
    },
    updateSeriesLine() {
      this.$refs.realtimeChartUserMention.updateOptions({
        xaxis: {
          categories: this.user_mentions.chartOptions.xaxis.categories,
        },
      });
      this.$refs.realtimeChartScreenNames.updateOptions({
        xaxis: {
          categories: this.screen_names.chartOptions.xaxis.categories,
        },
      });
      this.$refs.realtimeChartTopicResult.updateOptions({
        xaxis: {
          categories: this.topic_result.chartOptions.xaxis.categories,
        },
      });
    },
    dateFormat(d) {
      return `${d.getFullYear()}-${
        d.getMonth() + 1 < 10 ? "0" + (d.getMonth() + 1) : d.getMonth() + 1
      }-${d.getDate() < 10 ? "0" + d.getDate() : d.getDate()}`;
    },
    setDate(period) {
      var end = new Date();
      var start = new Date(new Date().valueOf() - 1000 * 60 * 60 * 24 * period);
      this.range = [start, end];
    },
    
  },
  computed:{
      activeFilters(){
        for(var filter of this.filters){
            this.active_filters.filters[filter.name] = {
            value: filter.select,
            };
        }
        this.active_filters.filters.Search = {
            value: this.search,
            
        };
        this.active_filters.filters.Topic = {
        value: this.topic_select.select,
       
      };
    }
  },

  components: {
    TwitterCard,
    apexchart: VueApexCharts,
    "stats-card": StatsCard,
        VueDatepickerLocal

  },
  
};
</script>

<style>
.section-header {
  color: white;
  font-size: 1.8rem;
  font-weight: bold;
}

.section-description {
  color: white;
  font-size: 1.3rem;
  line-height: 1.9rem;
}

.v-data-table-header th{
    background-color: #0F3357;
}

.v-data-table-header th span{
    color: white;
}

</style>

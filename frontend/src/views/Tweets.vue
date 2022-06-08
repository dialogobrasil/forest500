<template>
  <section class="tweets">
    <v-row class="ma-5">
      <v-col cols="12">
        <v-card class="ma-5 align-center" color="#21ACBF" dark>
          <v-card-title class="">
            <div class="">
              <span class="section-header"> Influencers </span>
            </div>

            <v-spacer></v-spacer>
          </v-card-title>
          <v-card-text class="section-description px-5" align="justify">
            Social media is all about connections and valuable interactions,
            that's why it's best represented and analysed as a network. Our
            network graph analysis is a live, browser-based interest graph,
            mapping the way people engage with each other and hashtags across
            Twitter. Affinities by mutual relationships and hashtags provide
            insights about community building, engagement relationship between
            two or multiple authors providing insights about influencers and
            communities online.
          </v-card-text>
        </v-card>
      </v-col>

      <v-col cols="12">
        <v-card class="mx-5 d-flex align-center">
              <v-autocomplete
                clear
                class="mx-5"
                label="topic"
                v-model="topic_select.select"
                :items="topic_select.items"
              ></v-autocomplete>
              <v-autocomplete
                clear
                class="mx-5"
                label="Network"
                v-model="type_select.select"
                :items="type_select.items"
              ></v-autocomplete>
              <v-autocomplete
                clear
                class="mx-5"
                label="Source Panel"
                v-model="institution_type.select"
                :items="institution_type.items"
              ></v-autocomplete>

              <vue-datepicker-local
                v-model="range"
                :local="local"
              ></vue-datepicker-local>
              <v-btn class="mx-5" text color="#0F3357" @click="getStatus()">
                HIT
              </v-btn>
        </v-card>
      </v-col>

    <v-col cols='12'>
      <v-card class="mx-5">
        <v-card-title>{{ description.title }}</v-card-title>
        <v-card-text v-html="description.text"></v-card-text>
      </v-card>
      <v-progress-circular v-show='loading'
      indeterminate
      color="primary"
    ></v-progress-circular>
    </v-col>

      <v-responsive min-height="100vh">
        <d3-network  :net-nodes="nodes" :net-links="links" :options="options" :v-show='loading'>
        </d3-network>
      </v-responsive>

    </v-row>
  </section>
</template>

<script>
import axios from "axios";
import TwitterCard from "../components/TwitterCard.vue";
import D3Network from "vue-d3-network";
import VueDatepickerLocal from "vue-datepicker-local";

export default {
  name: "Dashboard",
  data() {
    return {
      range: [new Date(2021, 6, 1), new Date(2021, 11, 1)],
      emptyTime: "",
      emptyRange: [],
      local: {
        dow: 0, // Sunday is the first day of the week
        hourTip: "Select Hour", // tip of select hour
        minuteTip: "Select Minute", // tip of select minute
        secondTip: "Select Second", // tip of select second
        yearSuffix: "", // suffix of head year
        monthsHead:
          "January_February_March_April_May_June_July_August_September_October_November_December".split(
            "_"
          ), // months of head
        months: "Jan_Feb_Mar_Apr_May_Jun_Jul_Aug_Sep_Oct_Nov_Dec".split("_"), // months of panel
        weeks: "Su_Mo_Tu_We_Th_Fr_Sa".split("_"), // weeks,
        cancelTip: "cancel",
        submitTip: "confirm",
      },
      user_mention_network: {
        title: "How was the user mentions network drawn?",
        text: `&nbsp;&nbsp;&nbsp;&nbsp;Nodes (Circles): users Twitter handle based on filter selection<br><br>
	            &nbsp;&nbsp;&nbsp;&nbsp;Link (Connection): users relations based on who mentions who. The link direction represents who mentioned who. Ex: A -> B, “User A” mentions “User B”.<br><br>
	            &nbsp;&nbsp;&nbsp;&nbsp;Node size: number of times a specific user appears in our database.`,
      },
      hashtag_network: {
        title: "How was the hashtag network drawn?",
        text: `&nbsp;&nbsp;&nbsp;&nbsp;Nodes (Circles): hashtags used by users on our database. <br><br>
	&nbsp;&nbsp;&nbsp;&nbsp;Link (Connection): the hashtag connections are representative of the mutual a simultaneously connection of two  hashtags in one single tweet.<br><br>
	&nbsp;&nbsp;&nbsp;&nbsp;Size of Nodes: number of times a hashtag appears in our database.`,
      },
      description: {
        title: "How was the hashtag network drawn?",
        text: `&nbsp;&nbsp;&nbsp;&nbsp;Nodes (Circles): hashtags used by users on our database. <br><br>
	&nbsp;&nbsp;&nbsp;&nbsp;Link (Connection): the hashtag connections are representative of the mutual a simultaneously connection of two  hashtags in one single tweet.<br><br>
	&nbsp;&nbsp;&nbsp;&nbsp;Size of Nodes: number of times a hashtag appears in our database.`,
      },
      nodes: [],
      links: [],
      nodeSize: 20,
      canvas: false,
      status: [],
      tab: null,
      search: null,
      loading: true,
      items: [
        { tab: "Companies", to: "/dashboard" },
        { tab: "Financial", to: "/financial" },
        { tab: "News", to: "/journalist" },
      ],
      dates: ["2021-01-01", "2021-08-31"],
      institution_type: {
        select: "Company",
        items: ["Company", "Financial", "Journalist"],
      },
      topic_select: {
        select: "nature",
        items: [
          "monitoring",
          "nature",
          "climate",
          "risks",
          "deforestation",
          "certification",
          "esg",
          "landuse",
          "sourcing",
          "protocol",
          "paper",
          "beef",
          "agenda",
          "social",
          "soy",
          "fires",
          "commodities",
          "palm",
        ],
      },
      type_select: {
        select: "Mentions",
        items: ["Mentions"],
      },
      menu: false,
      options: {
        force: 100,
        nodeLabels: true,
        strLinks: false,
        linkWidth: 1,
        fontSize: 12
      },
    };
  },
  mounted() {
    this.getStatus();
  },
  methods: {
    getStatus() {
      this.loading=true

      var url_query = `/api/v1/latest-status/?source_panel=${this.institution_type.select.toLowerCase()}&topic=${
        this.topic_select.select == "" ? "" : this.topic_select.select
      }&created_at_gte=${this.dateFormat(
        this.range[0]
      )}&created_at_lte=${this.dateFormat(this.range[1])}`;
      console.log(url_query);
      axios.get(url_query).then((res) => {
        console.log(res);

        this.nodes = res.data.nodes;
        this.links = res.data.links;

        this.description = this.user_mention_network;
        this.loading=false;
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

  components: {
    TwitterCard,
    D3Network,
    VueDatepickerLocal,
  },
};
</script>
<style src="vue-d3-network/dist/vue-d3-network.css">
</style>

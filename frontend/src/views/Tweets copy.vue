<template>
  <section class="tweets">

    <v-card class="ma-5 align-center" color="#21ACBF" dark >
      <v-card-title class="">

      <div class="">
        <span class="section-header"> Influencers </span>
      </div>

      <v-spacer></v-spacer>
    </v-card-title>
    <v-card-text class="section-description px-5" align="justify">
      Social media is all about connections and valuable interactions, that's why it's best represented and analysed as a network. Our network graph analysis is a live, browser-based interest graph, mapping the way people engage with each other and hashtags across Twitter. Affinities by mutual relationships and hashtags provide insights about community building, engagement relationship between two or multiple authors providing insights about influencers  and communities online. 
          </v-card-text>
    </v-card>

    <v-card class="ma-5 d-flex align-center">
      <v-autocomplete clear class="mx-5" label="topic" v-model="topic_select.select" :items="topic_select.items"></v-autocomplete>
      <v-autocomplete clear class="mx-5" label="Network" v-model="type_select.select" :items="type_select.items" ></v-autocomplete>
      <v-autocomplete clear class="mx-5" label="Source Panel" v-model="institution_type.select" :items="institution_type.items" ></v-autocomplete>
      <v-divider class="ma-2" vertical></v-divider>

 <vue-datepicker-local v-model="range" :local="local" ></vue-datepicker-local>
<v-btn class="mx-5" text color="#0F3357" @click="getStatus()">
        HIT
      </v-btn>
    </v-card>

    <v-row class='ma-5'>
    <v-col cols=9>
      <d3-network :net-nodes="nodes" :net-links="links" :options="options">
      </d3-network>
    </v-col>
    <v-col cols=3>
        <v-card>
            <v-card-title>{{description.title}}</v-card-title>
            <v-card-text v-html='description.text'></v-card-text>
        </v-card>
    </v-col>

    </v-row>
  </section>
</template>

<script>
import axios from "axios";
import TwitterCard from "../components/TwitterCard.vue";
import D3Network from 'vue-d3-network'
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
      user_mention_network: {
        title:"How was the user mentions network drawn?",
        text:`&nbsp;&nbsp;&nbsp;&nbsp;Nodes (Circles): users Twitter handle based on filter selection<br><br>
	            &nbsp;&nbsp;&nbsp;&nbsp;Link (Connection): users relations based on who mentions who. The link direction represents who mentioned who. Ex: A -> B, “User A” mentions “User B”.<br><br>
	            &nbsp;&nbsp;&nbsp;&nbsp;Node size: number of times a specific user appears in our database.`,
      },
      hashtag_network: {
        title:"How was the hashtag network drawn?",
        text:`&nbsp;&nbsp;&nbsp;&nbsp;Nodes (Circles): hashtags used by users on our database. <br><br>
	&nbsp;&nbsp;&nbsp;&nbsp;Link (Connection): the hashtag connections are representative of the mutual a simultaneously connection of two  hashtags in one single tweet.<br><br>
	&nbsp;&nbsp;&nbsp;&nbsp;Size of Nodes: number of times a hashtag appears in our database.`,
      },
    description: {
        title:"How was the hashtag network drawn?",
        text:`&nbsp;&nbsp;&nbsp;&nbsp;Nodes (Circles): hashtags used by users on our database. <br><br>
	&nbsp;&nbsp;&nbsp;&nbsp;Link (Connection): the hashtag connections are representative of the mutual a simultaneously connection of two  hashtags in one single tweet.<br><br>
	&nbsp;&nbsp;&nbsp;&nbsp;Size of Nodes: number of times a hashtag appears in our database.`,
      },
            nodes: [
      ],
      links: [
      ],
      nodeSize:20,
      canvas:false,
      status: [],
      tab: null,
      search: null,
      items: [
        { tab: "Companies", to: "/dashboard" },
        { tab: "Financial", to: "/financial" },
        { tab: "News", to: "/journalist" },
      ],
      dates: ["2021-01-01", "2021-08-31"],
      institution_type: {
        select: '',
        items: ['Company','Financial','Journalist'],
      },
      topic_select: {
        select: '',
        items: [],
      },
      type_select: {
        select: 'Hashtags',
        items: ['Mentions','Hashtags'],
      },
      menu: false,
options:
      {
        force: 1000,
        nodeSize: 20,
        nodeLabels: true,
        linkWidth:1
      }
    };
  },
  mounted() {
    this.getStatus();
  },
  methods: {
      getStatus() {
      var url_query = `api/v1/latest-status/?source_panel=${this.institution_type.select.toLowerCase()}topic=${
        this.topic_select.select == '' ? '' : this.topic_select.select
      }&created_at_gte=${
       this.dateFormat(this.range[0])
      }&created_at_lte=${this.dateFormat(this.range[1])}`;
      console.log(url_query)
      axios.get(url_query).then((res) => {
        var nodes_user = {}
        var final_nodes_user = []
        var links_user = []
        //nodes = res.data.results.map( (x) => x.user.screen_name )
        for (var i in res.data.results){
          nodes_user[res.data.results[i].user.id] = res.data.results[i].user.screen_name
          for( var j in res.data.results[i].user_mentions){
            nodes_user[res.data.results[i].user_mentions[j].id] = res.data.results[i].user_mentions[j].screen_name
            links_user.push({sid:res.data.results[i].user.id, tid:res.data.results[i].user_mentions[j].id})
          }
        }
        console.log(Object.keys(nodes_user).length)

        var arr_nodes_user = Object.keys(nodes_user)
        for(var i in arr_nodes_user){
          //console.log(nodes_user[arr_nodes_user[i]])
          final_nodes_user.push({id:arr_nodes_user[i], name:nodes_user[arr_nodes_user[i]]})
        }
        this.nodes = final_nodes_user
        this.links = links_user
        this.topic_select.items = 
          res.data.facets._filter_topic_set.topic_set.buckets.map(
            (x) => x.key
        );
        var nodes_hashtag = []
        var final_nodes_hashtag = []
        var links_hashtag = []
        //nodes = res.data.results.map( (x) => x.user.screen_name )
        for (var i in res.data.results){
          nodes_hashtag.push(res.data.results[i].hashtags.map(x => x.text))
        }
        var nodes_ids = {}
        var k = 0
        for (var i in nodes_hashtag){
          for (var j in nodes_hashtag[i]){

            if(!final_nodes_hashtag.map(x => x.id ).includes(nodes_hashtag[i][j]) )
              final_nodes_hashtag.push({id: nodes_hashtag[i][j], name:nodes_hashtag[i][j]})
            for (var x in nodes_hashtag[i]){
              if(nodes_hashtag[i][j] != nodes_hashtag[i][x]){
                links_hashtag.push({sid:nodes_hashtag[i][j], tid:nodes_hashtag[i][x]})
              }
            }
          }
        }

        if(this.type_select.select == 'Hashtags'){
          this.nodes = final_nodes_hashtag
          this.links = links_hashtag
          this.description = this.hashtag_network
        }
        else if(this.type_select.select == 'Mentions'){
          this.nodes = final_nodes_user
          this.links = links_user
          this.description = this.user_mention_network
        } else{
          this.nodes = []
          this.links = []
        }
        
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
    VueDatepickerLocal

  },
};
</script>
<style src="vue-d3-network/dist/vue-d3-network.css">


</style>

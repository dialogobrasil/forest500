<template>
  <v-container id="insights">
    <v-row class="mt-6" justify="center">
      <v-col cols="12" align="center">
        <span id="header"
          >Please, select the topic and the on question to get some
          insights</span
        >
      </v-col>
      <!-- <v-col align="right" cols="6">
        <span id="question">Which Companies are talking about</span>
      </v-col> -->
      <v-col cols="6" align="left">
        <v-select :items="items" label="Select a topic" solo></v-select>
      </v-col>
      <v-col cols="6" align="left">
        <v-select :items="items" label="Select a Question" solo></v-select>
      </v-col>
    </v-row>
    <v-row justify="center">
      <v-col cols="8">
             <v-sheet
        :color="`grey ${theme.isDark ? 'darken-2' : 'lighten-4'}`"
        class="pa-3"
      >
        <v-skeleton-loader
          class="mx-auto"
          max-width="300"
          type="card"
        ></v-skeleton-loader> </v-sheet>
      </v-col>
        </v-row>

      <hr class="mt-6"/>
  </v-container>

  
</template>

<script>
import VueApexCharts from "vue-apexcharts";

export default {
  name: "Insights",
  inject: {
    theme: {
      default: { isDark: false },
    },
  },
  data() {
    return {
      items: ["Deforestation", "Climate", "Fires", "ESG", "..."],
      options: {
        labels: ["Team A", "Team B", "Team C", "Team D", "Team E"],

        title: {
          text: "Top Companies by percentage of tweets",
          align: "center",
          margin: 10,
          offsetX: 0,
          offsetY: 0,
          floating: false,
          style: {
            fontSize: "14px",
            fontWeight: "bold",
            fontFamily: undefined,
            color: "#263238",
          },
        },

        chart: {
          id: "vuechart-example",
        },
      },
      series: [
        {
          data: [30, 40, 45, 50, 49, 60, 70, 91],
        },
      ],
    };
  },
  components: { apexchart: VueApexCharts },
};
</script>

<style >
#question {
  font-size: 30px;
}
#header {
  font-size: 2rem;
}
</style>
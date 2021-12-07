<template>
  <v-app style="background-color:#F0F0F0;">
    <v-app-bar app clipped-left color="#0F3357" dark>
        <span id="brand" >
          <Strong >HITS - Twitter Environmental Pulse</Strong>
        </span>

      <v-spacer></v-spacer>

      <router-link to="/">
        <v-btn text>
          <v-icon size=32>mdi-home</v-icon>
          <span class="ml-2">Home</span>
        </v-btn>
      </router-link>
      <router-link to="/dashboard">
        <v-btn text>
          <v-icon size=32>mdi-view-dashboard</v-icon>
          <span class="ml-2">Dashboards</span>
        </v-btn>
      </router-link>
      <router-link to="/insights">
        <v-btn text>
          <v-icon size=32>mdi-lightbulb-on</v-icon>
          <span class="ml-2">Insights</span>
        </v-btn>
      </router-link>
      <router-link to="/tweets">
        <v-btn text>
          <v-icon size=26>fa-project-diagram</v-icon>
          <span class="ml-2">Influencers</span>
        </v-btn>
      </router-link>
      <router-link to="/about">
        <v-btn text>
          <v-icon size=26>fa-user-cog</v-icon>
          <span class="ml-2">The Project</span>
        </v-btn>
      </router-link>

    </v-app-bar>

    <v-main>
      <router-view />
    </v-main>

  <v-footer padless>
    <v-col
      class="text-center"
      cols="12"
    >
     <strong>Food Nature Climate Dialogue (FNCD)</strong> - {{ new Date().getFullYear() }} 
    </v-col>
  </v-footer>
  </v-app>
</template>

<script>
import '@fortawesome/fontawesome-free/css/all.css' // Ensure you are using css-loader

export default {
icons: {
    iconfont: 'fa',
  },
  name: "App",

  data: () => ({
    //
  }),
};
</script>

<style >
@import url('https://fonts.googleapis.com/css?family=Merriweather');


html, body {
  font-family: 'Merriweather', sans-serif;
}

#app {
  font-family: 'Merriweather', sans-serif;
}

#brand{
  font-size: 1.4rem;
}

a{
text-decoration: none;
}


.v-main__wrap button{
  background-color: #21ADBF!important;
  color: white!important;
}

.section-header{
  color: white;
  font-size: 1.8rem;
  font-weight: bold;
}

.section-description{
  color: white;
  font-size:1.3rem!important;
  line-height: 1.9rem!important;
}

.datepicker-popup{
  display: flex;
  padding: 0px;
  margin-left: -20px;
}

</style>

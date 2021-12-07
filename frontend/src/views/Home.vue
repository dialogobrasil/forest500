<template>
  <section>
    <div class="ma-5">
    <span id="welcome-header" >
      Welcome to HITS - Twitter Environmental Pulse!
    </span>
    <span id="welcome-complement">
      What would you like to do? <br><br>&emsp;&emsp;Click in one of the applications or get to know our tool clicking in the project section.
    </span>
    </div>
    
<masonry class="ma-5"
:cols="{default: 2, 1000: 2, 700: 2, 400: 1}"
   >
  <div class="ma-2" >
<v-card class="ma-5" to="/dashboard" >
          <v-card class="pa-5" color="primary" dark flat>
            <h1>Dashboard</h1>
          </v-card>
          <v-card-text align="justify">
            <p>
              By addressing the challenge most organizations have on resources and staff the interactive dashboard is a flexible tool for customization providing  key trends, narratives and influencers.  
            </p>
          </v-card-text>
        </v-card>
  </div>
  <div class="ma-2" >
<v-card class="ma-5" to="/insights">
          <v-card class="pa-5" color="secondary" dark flat>
            <h1>Insights</h1>
          </v-card>
          <v-card-text align="justify">
            <p>
              The insights section is the perfect space for quick twitter hits, insights and graphics addressing questions related to the community behavior online and the topics connecting the environmental agenda. 
            </p>
          </v-card-text>
        </v-card>
  </div>
  <div class="ma-2" >
<v-card class="ma-5" to="/tweets" >
          <v-card class="pa-5" color="teal" dark flat>
            <h1>Influencers</h1>
          </v-card>
          <v-card-text align="justify">
            <p>
Have a look at our Influencer Network and discover how hashtags and mentions connections could help you.              </p>
          </v-card-text>
        </v-card>
  </div>
  <div class="ma-2" >
<v-card class="ma-5" to="/about">
          <v-card class="pa-5" color="orange" dark flat>
            <h1>The Project</h1>
          </v-card>
          <v-card-text align="justify">
            <p>
              Twitter Environmental Pulse is a technology for monitoring and analyzing Twitter trends that uses selective curation to increase discovery of relevant conversations and debates. 
            </p>
          </v-card-text>
        </v-card>
  </div>
  <!-- <div class="ma-2" >
<v-card class="ma-5" >
          <v-card class="pa-5" color="indigo" dark flat>
            <h1>Quick Hits</h1>
          </v-card>
          <v-card-text align="justify">
            <p>
              Launch a search by typing in your keyword(s)
            </p>
          </v-card-text>
          <v-card-actions>
            
          <v-icon>mdi-magnify</v-icon>
          </v-card-actions>
        </v-card>
  </div> -->
</masonry>

    <!-- <v-row>
      <v-col cols="4">
        <v-card class="ma-5" >
          <v-card class="pa-5" color="primary" dark flat>
            <h1>View Dashboards</h1>
          </v-card>
          <v-card-text align="justify">
            <p>
              By addressing the challenge most organizations have on resources and staff the interactive dashboard is a flexible tool for customization providing  key trends, narratives and influencers.  
            </p>
          </v-card-text>
        </v-card>
      </v-col>
      <v-col cols="4">
        <v-card class="ma-5" >
          <v-card class="pa-5" color="secondary" dark flat>
            <h1>Insights</h1>
          </v-card>
          <v-card-text align="justify">
            <p>
              The insights section is the perfect space for quick twitter hits, insights and graphics addressing questions related to the community behavior online and the topics connecting the environmental agenda. 
            </p>
          </v-card-text>
        </v-card>
      </v-col>
      <v-col cols="4">
        <v-card class="ma-5" >
          <v-card class="pa-5" color="teal" dark flat>
            <h1>Networks</h1>
          </v-card>
          <v-card-text align="justify">
            <p>
              Social media is all about connections and valuable interactions, that's why it's best represented and analysed as a network. Our network graph analysis is a live, browser-based interest graph, mapping the way people engage with each other across Twitter. Affinities by mutual relationships and topics provides insights about community building, engagement relationship between two or multiple authors providing insights about influencers  and communities online.
            </p>
          </v-card-text>
        </v-card>
      </v-col>
      <v-col cols="4">
        <v-card class="ma-5" >
          <v-card class="pa-5" color="orange" dark flat>
            <h1>About the Project</h1>
          </v-card>
          <v-card-text align="justify">
            <p>
              Twitter Environmental Pulse is a technology for monitoring and analyzing Twitter trends that uses selective curation to increase discovery of relevant conversations and debates. 
            </p>
          </v-card-text>
        </v-card>
      </v-col>
      <v-col cols="8">
        <v-card class="ma-5" max-width="800">
          <v-card class="pa-5" color="indigo" dark flat>
            <h1>Quick search</h1>
          </v-card>
          <v-card-text align="justify">
            <p>
              Lorem Ipsum is simply dummy text of the printing and typesetting
              industry. Lorem Ipsum has been the industry's standard dummy text
              ever since the 1500s, when an unknown printer took a galley of
              type and scrambled it to make a type specimen book.
            </p>
          </v-card-text>
          <v-card-actions>
          <v-icon>mdi-magnify</v-icon>
          </v-card-actions>
        </v-card>
      </v-col>
    </v-row> -->
  </section>
</template>

<script>
export default {};
</script>

<style>
  #welcome-header{
    font-size:1.7rem;
    font-weight: bold;
  }

  #welcome-complement{
    font-size: 1.3rem;
  }

  p{
    font-size: 1.2rem;
    line-height: 1.9rem;
  }

  h1{
    font-size: 2rem;
  }
  

</style>
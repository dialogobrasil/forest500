<template>
  <v-container class="about">
    <v-row class="ma-5" v-for="item in items" :key="item.name">
      <v-col cols="12">
        <h1 class="text-center">{{ item.name }}</h1>
      </v-col>
      <v-col v-for="text in item.text" :key="text.header" :cols="text.size">
        <h3>{{ text.header }}</h3>
        <div class="mt-2" v-html="text.content"></div>
      </v-col>
      <v-col class="mt-6" cols=12>
      <v-divider></v-divider>
      </v-col>
    </v-row>

    <!-- <div class="ma-5" v-for="item in items"
        :key="item.name">
        <h1>{{ item.name}}</h1>
            <masonry class="ma-5" :cols="{ default: 3, 1000: 2, 700: 2, 400: 1 }">
              <v-card v-for="text in item.text"
              :key="text.header" class="ma-5">
                <v-card class="pa-2" :color="text.color" dark flat>
                  <h1>{{text.header}}</h1>
                </v-card>
                <v-card-text align="left">
                      <div v-html="text.content"></div>
                </v-card-text>
              </v-card>
            </masonry>
    </div> -->

    <!-- <v-tabs
      color="deep-purple accent-4"
      right
    >
      <v-tab v-for="item in items" :key="item.name">{{item.name}}</v-tab>

      <v-tab-item
        v-for="item in items"
        :key="item.name"
      >
          <v-row>
            <v-col
              v-for="text in item.text"
              :key="text.header"
              cols="12"
              md="4"
            >
              <v-card class="ma-5" max-width="400">
                <v-card class="pa-2" :color="text.color" dark flat>
                  <h1>{{text.header}}</h1>
                </v-card>
                <v-card-text align="left">
                      <div v-html="text.content"></div>
                </v-card-text>
              </v-card>
            </v-col>
          </v-row>
      </v-tab-item>
    </v-tabs> -->
  </v-container>
</template>

<script>
export default {
  name: "About",
  data() {
    return {
      items: [
        {
          name: "HITS - Twitter Environmental Pulse",
          text: [
            {
              header: null,
              content:
                "HITS - Twitter Environmental Pulse is a tool for monitoring and analyzing Twitter trends that uses selective curation to increase discovery of relevant influencers, conversations, debates about climate, forests and social environmental issues. By tracking tweets, hashtags and relevant profiles on Twitter our suite of tools allows digital strategists to track how narratives, stories and ideas spread through Twitter. Our tools are designed to aggregate, analyze, deliver and visualize information, answering complex quantitative and qualitative questions about the climate and social environmental public debate.",
              color: "primary",
              size: "12",
            },
            {
              header: null,
              content:
                "HITS - Twitter Environmental Pulse is part of the digital intelligence, open-source and innovation initiative developed by the Food Nature Climate Dialogue with support of Global Canopy.",
              color: "secondary",
              size: "12",
            },
          ],
        },
        {
          name: " Why HITS - Twitter Environmental Pulse is relevant to your organization?",
          text: [
            {
              header: null,
              content:
                "Twitter is a central platform for the climate justice and environmental movement. Nevertheless, digital strategy today is part of  an overflowing  public sphere. News media, journalists, policy makers, secretariat, multilateral agencies, civil society organizations, politicians and the industry are part of Twitter and use this platform strategically to position themselves. The modern propaganda model is highly participatory and networked and here's where <strong>HITS - Twitter Environmental Pulse</strong> can support you and your team with quick insights and trend analysis. Our Twitter source panel is highly refined by our collaborators and experts on environmental issues, such as climate and energy, forests, land use, indigenous rights and related topics. ",
              color: "primary",
              size: "12",
            },
            {
              header: null,
              content:
                "The HITS - Twitter Environmental Pulse allows the development of a social media listening tool based on the curation of selected twitter profiles, filtered by key topics and pre-defined tags showing only the content that really matters.  Using its own analysis and discovery metrics, the technology allows monitoring of social network communities, quick insights and trend analysis, discovering new issues, mapping your audience and influencers, monitoring authorities and relevant profiles.",
              color: "secondary",
              size: "12",
            },
          ],
        },
        {
          name: "How can you use the quick HITS, dashboards, insights and network mapping in your strategic communications approach? ",
          text: [
            {
              header: "Quick HITS (TBA)",
              color: "primary",
              size: "6",

              content:
                "When logging into Quick Hits, you can search within the curated source panels database for a keyword, topic or hashtags to see how these are trending. ",
            },
            {
              header: "Dashboards",
              color: "secondary",
              size: "6",

              content:
                "Select a source panel and get instant social intelligence tailored to your specific digital needs. By addressing the challenge most organizations have on resources and staff the interactive dashboard is a flexible tool for customization providing key trends, narratives and influencers on Twitter.",
            },
            {
              header: "Insights",
              color: "teal",
              size: "6",

              content:
                "The insights section is the perfect space for quick twitter hits, insights and graphics addressing questions related to the community behavior online and the topics connecting the climate, forests and social environmental agenda. ",
            },
            {
              header: "Influencers",
              size: "6",

              color: "orange",
              content:
                "Social media is all about connections and valuable interactions, that's why it's best represented and analysed as a network. Our network graph analysis is a live, browser-based interest graph, mapping the way people engage with each other and hashtags across Twitter. Affinities by mutual relationships and hashtags provide insights about community building, engagement relationship between two or multiple authors providing insights about influencers and communities online.",
            },
          ],
        },
        {
          name: "Methods",
          text: [
            {
              header: "Selection",
              color: "primary",
              size: "6",

              content:
                "Global Canopy selects a list of Companies and Financial Institutions and related Journalists with respective twitter handles, being 350 companies and 150 institutions to evaluate the accountability of these institutions on twitter.Was created filters based on these institutions.<br><br> The related informations can be viewed <a href='https://docs.google.com/spreadsheets/d/1Y5rktiNanKsgNff4u42JjiI4xCS59J-p/edit?pli=1#gid=625592309' target='_blank' rel='noopener'>here</a>",
            },
            {
              header: "Data Collection",
              color: "secondary",
              size: "6",

              content:
                "Based on Selection list, was collected tweets and quotes of each institution since 2010 on Twitter.<br>Was stored every field available on Tweet Object.<br>The database has a 20 minute delay.",
            },
            {
              header: "Topic classification",
              color: "teal",
              size: "6",

              content:
                "All topic filters were provided by an full text search using Apache Lucene query, all queries can be consulted <a href='topics.csv' download>here</a>",
            },
            {
              header: "Source Code",
              size: "6",

              color: "orange",
              content:
                "The Source code of this project is under GPL3 license avaliable on <a href='https://github.com/dialogobrasil/forest500-backend' target='_blank' rel='noopener'>Github</a>",
            },
          ],
        },
        {
          name: "Project team",
          text: [
            {
              header: "Food Nature Climate Dialogue (FNCD)",
              color: "primary",
              content:
                "Lori Regattieri – Project Coordination, UX design and digital storytelling<br>Luiz Tavares – Lead IT Developer, data visualization and web design",
            },
            {
              header: "Colaborator – Global Canopy and Forest 500",
              color: "secondary",
              content: "Daisy Payne – Project coordination, communication and research design<br>Henrietta Flodell – Research support<br>Bradley Graham – Operations support",
            },
          ],
        },
      ],
    };
  },
};
</script>

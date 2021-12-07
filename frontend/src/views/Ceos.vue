<template>
  <section>
     <v-navigation-drawer
      color="#0F3357"
      dark
      permanent
      clipped
      app
      width="10%"
      :style="{ top: $vuetify.application.top + 'px', zIndex: 4 }"
    >
      <v-list dense nav>
        <v-list-item v-for="item in items" :key="item.tab" link :to="item.to" >
          <v-list-item-content >
            <v-list-item-title>{{ item.tab }}</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>


    <v-card class="ma-5 d-flex align-center">
      <v-text-field
        class="mx-5"
        @keyup="getStatus()"
        filled
        dense
        label="Search"
        v-model="search"
      ></v-text-field>
      <v-select class="mx-5" label="topic"> </v-select>
      <v-divider class="mx-5" vertical></v-divider>
      <v-btn class="mx-2">1D</v-btn>
      <v-btn class="mx-2">7D</v-btn>
      <v-btn class="mx-2">30D</v-btn>

      <v-menu
        class=""
        ref="menu"
        v-model="menu"
        :close-on-content-click="false"
        :return-value.sync="dates"
        transition="scale-transition"
        offset-y
        min-width="auto"
      >
        <template v-slot:activator="{ on, attrs }">
          <v-combobox
            class="mx-5"
            v-model="dates"
            multiple
            label="Multiple picker in menu"
            prepend-icon="mdi-calendar"
            readonly
            v-bind="attrs"
            v-on="on"
          ></v-combobox>
        </template>
        <v-date-picker v-model="dates" range no-title scrollable>
          <v-spacer></v-spacer>
          <v-btn text color="#0F3357" @click="menu = false"> Cancel </v-btn>
          <v-btn text color="#0F3357" @click="$refs.menu.save(dates)">
            OK
          </v-btn>
        </v-date-picker>
      </v-menu>
      <v-dialog v-model="dialog" persistent max-width="600px">
        <template v-slot:activator="{ on, attrs }">
          <v-btn color="#0F3357" class="mr-5" dark v-bind="attrs" v-on="on">
            Filters
          </v-btn>
        </template>
        <v-card>
          <v-card-title>
            <span class="text-h5">CEOs Filters</span>
          </v-card-title>
          <v-card-text>
            <v-container>
              <v-row>
                <v-col cols="12" sm="6">
                  <v-autocomplete
                    :items="[
                      'Skiing',
                      'Ice hockey',
                      'Soccer',
                      'Basketball',
                      'Hockey',
                      'Reading',
                      'Writing',
                      'Coding',
                      'Basejump',
                    ]"
                    label="Name"
                    multiple
                  ></v-autocomplete>
                </v-col>
                <v-col cols="12" sm="6">
                  <v-autocomplete
                    :items="[
                      'Skiing',
                      'Ice hockey',
                      'Soccer',
                      'Basketball',
                      'Hockey',
                      'Reading',
                      'Writing',
                      'Coding',
                      'Basejump',
                    ]"
                    label="Headquarters"
                    multiple
                  ></v-autocomplete>
                </v-col>
                 <v-col cols="12" sm="6">
                  <v-autocomplete
                    :items="[
                      'Skiing',
                      'Ice hockey',
                      'Soccer',
                      'Basketball',
                      'Hockey',
                      'Reading',
                      'Writing',
                      'Coding',
                      'Basejump',
                    ]"
                    label="Commodities"
                    multiple
                  ></v-autocomplete>
                </v-col>   
                 <v-col cols="12" sm="6">
                  <v-autocomplete
                    :items="[
                      'Skiing',
                      'Ice hockey',
                      'Soccer',
                      'Basketball',
                      'Hockey',
                      'Reading',
                      'Writing',
                      'Coding',
                      'Basejump',
                    ]"
                    label="Financial Institution Type"
                    multiple
                  ></v-autocomplete>
                </v-col>   
                <v-col cols="12" sm="6">
                  <v-autocomplete
                    :items="[
                      'Skiing',
                      'Ice hockey',
                      'Soccer',
                      'Basketball',
                      'Hockey',
                      'Reading',
                      'Writing',
                      'Coding',
                      'Basejump',
                    ]"
                    label="Sustainability commitments"
                    multiple
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
    </v-card>

      <div class="text-center">

    <v-chip
      class="ma-0"
      color="transparent"
      label
      text-color="black"
      x-large
    >
      <v-icon left>
        mdi-filter
      </v-icon>
      Active Filters: 
    </v-chip>

    <v-chip
      class="ma-2"
      color="#0F3357"
      label
    >
      <v-icon left>
        mdi-account-circle-outline
      </v-icon>
      John Leider
    </v-chip>

    <v-chip
      class="ma-2"
      close
      color="cyan"
      label
      text-color="white"
    >
      <v-icon left>
        mdi-twitter
      </v-icon>
      New Tweets
    </v-chip>
  </div>

  <v-divider
  
></v-divider>

  </section>
</template>

<script>
import axios from "axios";
import TwitterCard from "../components/TwitterCard.vue";

export default {
  name: "Dashboard",
  data() {
    return {
      status: [],
      tab: null,
      search: null,
      dates: ["2019-09-10", "2019-09-20"],
      menu: false,
      dialog: false,
      items: [
        { tab: "Companies", to: "/dashboard" },
        { tab: "Financial", to: "/financial" },
        { tab: "CEOs", to: "/ceos"  },
        { tab: "Journalists", to: "/journalist"  },
      ],
      filters: [
        { name: "Topic" },
        { name: "Section" },
        { name: "Subsidary" },
        { name: "Brands" },
        { name: "Commodities" },
        { name: "Segments" },
        { name: "Signatories" },
      ],
    };
  },
  mounted() {
    // this.getStatus();
  },
  methods: {
    getStatus() {
      if (this.search == null || this.search == "")
        axios.get(`/search/status/`).then((res) => {
          this.status = res.data.results;
        });
      else
        axios.get(`/search/status/?search=${this.search}`).then((res) => {
          this.status = res.data.results;
        });
    },
  },

  components: {
    TwitterCard,
  },
};
</script>

<template>
      <v-card class="ma-10">
      <v-card-title class="align-start">
        <span class="font-weight-bold" style="font-size:24px">Overview</span>
        <v-spacer></v-spacer>
      </v-card-title>

      <v-card-subtitle class="mb-8 mt-n5">
        <span class="font-weight-semibold text--primary me-1"
          >Selected filters overview</span
        >
        <span></span>
      </v-card-subtitle>

      <v-card-text>
        <v-row>
          <v-col
            v-for="data in statisticsData"
            :key="data.title"
            cols="6"
            md="2"
            class="d-flex align-center"
          >
            <v-avatar
              size="44"
              color="primary"
              rounded
              class="elevation-1"
            >
              <v-icon dark color="white" size="30">
                {{data.icon}}
              </v-icon>
            </v-avatar>
            <div class="ms-3">
              <p class="text-xs mb-0">
                {{ data.title }}
              </p>
              <h3 class="text-xl font-weight-semibold">
                {{ data.total }}
              </h3>
            </div>
          </v-col>
        </v-row>
      </v-card-text>
    </v-card>
</template>

<script>
export default {
    props:[
        'statisticsData'
    ]
}
</script>

<style>

</style>
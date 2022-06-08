import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: () => import(/* webpackChunkName: "about" */ '../views/Home.vue')
  },
  {
    path: '/dashboard',
    name: 'Dashboaard',
    component: () => import(/* webpackChunkName: "about" */ '../views/Dashboard.vue')
  },
  {
    path: '/financial',
    name: 'Financial',
    component: () => import(/* webpackChunkName: "about" */ '../views/Financial.vue')
  },
  {
    path: '/ceos',
    name: 'CEOs',
    component: () => import(/* webpackChunkName: "about" */ '../views/Ceos.vue')
  },
  {
    path: '/journalist',
    name: 'Journarlist',
    component: () => import(/* webpackChunkName: "about" */ '../views/Journalist.vue')
  },
  {
    path: '/insights',
    name: 'Insights',
    component: () => import(/* webpackChunkName: "about" */ '../views/Insights.vue')
  },
  {
    path: '/methodologies',
    name: 'Methodologies',
    component: () => import(/* webpackChunkName: "about" */ '../views/Methodologies.vue')
  },
  {
    path: '/about',
    name: 'About',
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  },
  {
    path: '/dossie',
    name: 'Dossie',
    component: () => import(/* webpackChunkName: "about" */ '../views/Dossie.vue')
  },
  {
    path: '/tweets',
    name: 'Tweets',
    component: () => import(/* webpackChunkName: "about" */ '../views/Tweets.vue')
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router

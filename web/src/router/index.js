/** @format */

import Vue from "vue";
import VueRouter from "vue-router";

Vue.use(VueRouter);

// Application Routes
const routes = [
  {
    path: "/",
    name: "HomePage",
    component: () => import("../views/HomePage.vue"),
    meta: {
      requiresAuth: false,
    },
  },
  {
    path: "/p/:id",
    name: "CodePage",
    component: () => import("../views/CodePage.vue"),
    meta: {
      requiresAuth: false,
    },
  },
  {
    path: "/404",
    name: "NotFoundPage",
    component: () => import("../views/NotFoundPage.vue"),
    meta: {
      requiresAuth: false,
    },
  },
  {
    path: "/500",
    name: "ErrorPage",
    component: () => import("../views/ErrorPage.vue"),
    meta: {
      requiresAuth: false,
    },
  },
  {
    path: "*",
    redirect: "/404",
  },
];

const router = new VueRouter({
  routes,
});

// Auth Middleware
router.beforeEach((to, from, next) => {
  if (to.matched.some((record) => record.meta.requiresAuth)) {
    //~
  }
  next();
});

export default router;

/** @format */

import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import axios from "axios";
import Buefy from "buefy";
import "buefy/dist/buefy.css";
import Vuex from "vuex";
import store from "./store";
import VueCodemirror from "vue-codemirror";

// import base style
import "codemirror/lib/codemirror.css";

Vue.use(Vuex);

Vue.use(Buefy, { defaultIconPack: "fas" });

Vue.use(VueCodemirror);

Vue.config.productionTip = false;

Vue.prototype.$http = axios;

new Vue({
  store: store,
  router,
  render: (h) => h(App),
}).$mount("#app");

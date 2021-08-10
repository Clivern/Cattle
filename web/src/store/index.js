/** @format */

import Vue from "vue";
import Vuex from "vuex";
import api_server from "./api_server.module";

Vue.use(Vuex);

export default new Vuex.Store({
  modules: {
    api_server,
  },
});

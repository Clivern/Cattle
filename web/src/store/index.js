/** @format */

import Vue from "vue";
import Vuex from "vuex";
import api from "./api.module";

Vue.use(Vuex);

export default new Vuex.Store({
  modules: {
    api,
  },
});

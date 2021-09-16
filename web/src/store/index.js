/** @format */

import Vue from "vue";
import Vuex from "vuex";
import api_server from "./api_server.module";
import auth from "./auth.module";

Vue.use(Vuex);

export default new Vuex.Store({
	modules: {
		api_server,
		auth,
	},
});

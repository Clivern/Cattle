/** @format */

import {
	getApiServerReadiness,
	getApiServerHealth,
} from "@/common/api_server.api";

const state = () => ({
	readiness: {},
	health: {},
});

const getters = {
	getApiServerReadiness: (state) => {
		return state.readiness;
	},
	getApiServerHealth: (state) => {
		return state.health;
	},
};

const actions = {
	async fetchApiServerReadiness({ commit }) {
		const result = await getApiServerReadiness();
		commit("SET_API_SERVER_READINESS", result.data);
		return result;
	},

	async fetchApiServerHealth({ commit }) {
		const result = await getApiServerHealth();
		commit("SET_API_SERVER_HEALTH", result.data);
		return result;
	},
};

const mutations = {
	SET_API_SERVER_READINESS(state, readiness) {
		state.readiness = readiness;
	},
	SET_API_SERVER_HEALTH(state, health) {
		state.health = health;
	},
};

export default {
	namespaced: true,
	state,
	getters,
	actions,
	mutations,
};

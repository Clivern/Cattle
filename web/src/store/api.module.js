/** @format */

import {
  getAction,
  deleteAction,
  postAction,
  putAction,
} from "@/common/utils.api";

const state = () => ({
  result: {},
});

const getters = {
  getResult: (state) => {
    return state.result;
  },
};

const actions = {
  async get({ commit }, payload) {
    const result = await getAction(payload["uri"]);
    commit("SET_API_RESULT", result.data);
    return result;
  },
  async post({ commit }, payload) {
    const result = await postAction(payload["uri"], payload["request"]);
    commit("SET_API_RESULT", result.data);
    return result;
  },
  async put({ commit }, payload) {
    const result = await putAction(payload["uri"], payload["request"]);
    commit("SET_API_RESULT", result.data);
    return result;
  },
  async delete({ commit }, payload) {
    const result = await deleteAction(payload["uri"]);
    commit("SET_API_RESULT", result.data);
    return result;
  },
};

const mutations = {
  SET_API_RESULT(state, result) {
    state.result = result;
  },
};

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations,
};

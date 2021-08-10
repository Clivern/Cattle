/** @format */

import axios from "axios";

const ApiService = {
  getURL(endpoint) {
    let apiURL = "";

    if (process.env.VUE_API_SERVER_URL) {
      apiURL = process.env.VUE_API_SERVER_URL.replace(/\/$/, "");
    }

    return apiURL + endpoint;
  },

  getHeaders() {
    return {
      crossdomain: true,
      headers: {
        "X-Client-ID": "dashboard",
        "X-Requested-With": "XMLHttpRequest",
        "Content-Type": "application/json",
      },
    };
  },

  get(endpoint) {
    return axios.get(this.getURL(endpoint), this.getHeaders());
  },

  delete(endpoint) {
    return axios.delete(this.getURL(endpoint), this.getHeaders());
  },

  post(endpoint, data = {}) {
    return axios.post(this.getURL(endpoint), data, this.getHeaders());
  },

  put(endpoint, data = {}) {
    return axios.put(this.getURL(endpoint), data, this.getHeaders());
  },
};

export default ApiService;

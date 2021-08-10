/** @format */

import ApiService from "./api.service.js";

const getAction = (uri) => {
  return ApiService.get(uri);
};

const postAction = (uri, payload) => {
  return ApiService.post(uri, payload);
};

const putAction = (uri, payload) => {
  return ApiService.put(uri, payload);
};

const deleteAction = (uri) => {
  return ApiService.delete(uri);
};

export { getAction, deleteAction, postAction, putAction };

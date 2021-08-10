/** @format */

import ApiService from "./api.service.js";

const executeCodeAction = (payload) => {
  return ApiService.post("/api/v1/execute", payload);
};

const createCodeAction = (payload) => {
  return ApiService.post("/api/v1/code", payload);
};

const getCodeAction = (slug) => {
  return ApiService.get("/api/v1/code/" + slug);
};

const deleteCodeAction = (id, token) => {
  return ApiService.delete("/api/v1/code/" + id + "?token=" + token);
};

const updateCodeAction = (id, payload) => {
  return ApiService.put("/api/v1/code/" + id, payload);
};

const runCodeAction = (id) => {
  return ApiService.delete("/api/v1/code/" + id + "/run");
};

const getTaskAction = (id) => {
  return ApiService.get("/api/v1/task/" + id);
};

export {
  executeCodeAction,
  createCodeAction,
  getCodeAction,
  deleteCodeAction,
  updateCodeAction,
  runCodeAction,
  getTaskAction,
};

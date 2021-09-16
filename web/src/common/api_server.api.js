/** @format */

import ApiService from "./api.service.js";

const getApiServerReadiness = () => {
	return ApiService.get("/_ready");
};

const getApiServerHealth = () => {
	return ApiService.get("/_health");
};

export { getApiServerReadiness, getApiServerHealth };

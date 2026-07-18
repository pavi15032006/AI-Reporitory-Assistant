import axios from "axios";

const API = axios.create({
    baseURL: "https://ai-reporitory-assistant-1.onrender.com"
});

export default API;
import axios from "axios";
import state from "../../redux-toolkit"
let config;

const url = process.env.REACT_APP_API_URL;  

const setAuth = () => {
    config = {
        headers: {
            'Authorization': 'Bearer ' + state.getState().logged.token,
        }
    }
}

export const login = async (formData) => {
    return await axios.post(`${url}/auth/login`, formData);
}

export const registerUser = async (formData) => {
    return await axios.post(`${url}/auth/register`, formData);
}

export const getAllComments = async () => {
    setAuth();
    return await axios.get(`${url}/comments`, config);
}

export const postComment = async (formData) => {
    setAuth();
    return await axios.post(`${url}/comments`, formData, config)
}

export const getUserData = async (id) => {
    setAuth();
    return await axios.get(`${url}/histories?user=${id}`, config);
}

export const postUserData = async (formData) => {
    setAuth();
    return await axios.post(`${url}/histories`, formData, config);
}

export const getBearish = async () => {
    setAuth();
    return await axios.get(`${url}/stats/6372743e0d144d7f16b389f8`, config);
}

export const patchBearish = async (data) => {
    setAuth();
    return await axios.patch(`${url}/stats/6372743e0d144d7f16b389f8`, data, config)
}

export const fetchTweets = async () => {
    setAuth();
    return await axios.post(`${url}/twitter`, {tweet: 'stock'}, config);
}
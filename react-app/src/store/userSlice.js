import { createSlice } from '@reduxjs/toolkit';
import axios from 'axios';

const initialState = {
    loading: false,
    data: null,
    error: null
};

const userSlice = createSlice({
    name: 'user',
    initialState,
    reducers: {
        loginRequest: state => {
            state.loading = true;
            state.error = null;
        },
        loginSuccess: (state, action) => {
            state.loading = false;
            state.data = action.payload;
        },
        loginFailure: (state, action) => {
            state.loading = false;
            state.error = action.payload;
        }
    }
});

export const loginUser = (data) => async (dispatch) => {
    dispatch(loginRequest());

    try {
        const response = await axios.post('api/auth/login', data);
        dispatch(loginSuccess(response.data));
    } catch (error) {
        dispatch(loginFailure(error.response.data));
    }
};

export const signUpUser = (data) => async (dispatch) => {
    dispatch(loginRequest());
    try {
        const response = await axios.post('api/auth/signup', data);
        dispatch(loginSuccess(response.data));
    } catch (error) {
        dispatch(loginFailure(error.response.data));
    }
}

export const { loginRequest, loginSuccess, loginFailure } = userSlice.actions;
export default userSlice.reducer;

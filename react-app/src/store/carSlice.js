import { createSlice } from '@reduxjs/toolkit';
import axios from 'axios';

const initialState = {
    loading: false,
    data: null,
    error: null
};

const carSlice = createSlice({
    name: 'cars',
    initialState,
    reducers: {
        searchRequest: state => {
            state.loading = true;
            state.error = null;
        },
        searchSuccess: (state, action) => {
            state.loading = false;
            state.data = action.payload;
        },
        searchFailure: (state, action) => {
            state.loading = false;
            state.error = action.payload;
        }
    }
});

export const searchAvailableCars = (data) => async (dispatch) => {
    dispatch(searchRequest());
    try {
        const response = await axios.post('api/search/available_cars/' + parseInt(data.location), data);
        dispatch(searchSuccess(response.data))
    } catch (error) {
        dispatch(searchFailure(error));
    }
};

export const { searchRequest, searchSuccess, searchFailure } = carSlice.actions;
export default carSlice.reducer;

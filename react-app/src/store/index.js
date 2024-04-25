import { configureStore } from '@reduxjs/toolkit';
import userReducer from './userSlice';
import { thunk } from 'redux-thunk';

const middleware = [thunk];

const store = configureStore({
    reducer: {
        user: userReducer
    },
    middleware: () => middleware
});
export default store;

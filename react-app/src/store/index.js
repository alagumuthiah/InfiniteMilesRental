import { configureStore } from '@reduxjs/toolkit';
import userReducer from './userSlice';
import carReducer from './carSlice';

import { thunk } from 'redux-thunk';

const middleware = [thunk];

const store = configureStore({
    reducer: {
        user: userReducer,
        cars: carReducer
    },
    middleware: () => middleware
});
export default store;

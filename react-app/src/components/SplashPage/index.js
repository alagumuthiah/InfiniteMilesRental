import './SplashPage.css';
import { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { useDispatch, useSelector } from 'react-redux';
import { searchAvailableCars } from '../../store/carSlice';

const SplashPage = () => {

    const [location, setLocation] = useState('');
    const [pickupTime, setPickupTime] = useState('');
    const [pickupDate, setPickupDate] = useState('');
    const [dropTime, setDropTime] = useState('');
    const [dropDate, setDropDate] = useState('');

    const dispatch = useDispatch();
    const navigate = useNavigate();
    const userInfo = useSelector((state) => state.user);
    const available_cars = useSelector((state) => state.cars);

    useEffect(() => {
        if (available_cars?.data) {
            navigate("/search");
        }
    }, [navigate, available_cars])

    const handleSubmit = (event) => {
        event.preventDefault();
        const payload = {
            location,
            pickupDate,
            pickupTime,
            dropDate,
            dropTime
        }
        dispatch(searchAvailableCars(payload));
    }

    return (
        <>
            <div>
                <h2 className="mt-10 text-center text-2xl font-bold text-gray-900">
                    Navigate Your Adventure: Where Every Mile Tells a Story!
                </h2>
                <h3>Hello {userInfo?.data?.firstName}, {userInfo?.data?.lastName}</h3>
            </div>
            <div className="sm:mx-auto sm:w-full sm:max-w-sm">
                <form className="space-y-6" onSubmit={handleSubmit}>
                    <div>
                        <label htmlFor="location" className="block text-md font-medium leading-6 text-gray-900">
                            Location
                        </label>
                        <div className="mt-2">
                            <input
                                id="location"
                                name="location"
                                type="text"
                                required
                                value={location}
                                onChange={(event) => setLocation(event.target.value)}
                                className="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-custom-blue sm:text-sm sm:leading-6"
                            />
                        </div>
                    </div>
                    <div>
                        <label htmlFor="pickupDate" className="block text-md font-medium leading-6 text-gray-900">
                            PickUp Date
                        </label>
                        <div className="mt-2">
                            <input
                                id="pickupDate"
                                name="pickupDate"
                                type="date"
                                required
                                value={pickupDate}
                                onChange={(event) => setPickupDate(event.target.value)}
                                className="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-custom-blue sm:text-sm sm:leading-6"
                            />
                        </div>
                    </div>
                    <div>
                        <label htmlFor="pickupTime" className="block text-md font-medium leading-6 text-gray-900">
                            PickUp Time
                        </label>
                        <div className="mt-2">
                            <input
                                id="pickupTime"
                                name="pickupTime"
                                type="time"
                                required
                                value={pickupTime}
                                onChange={(event) => setPickupTime(event.target.value)}
                                className="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-custom-blue sm:text-sm sm:leading-6"
                            />
                        </div>
                    </div>
                    <div>
                        <label htmlFor="dropDate" className="block text-md font-medium leading-6 text-gray-900">
                            Drop Date
                        </label>
                        <div className="mt-2">
                            <input
                                id="dropDate"
                                name="dropDate"
                                type="date"
                                required
                                value={dropDate}
                                onChange={(event) => setDropDate(event.target.value)}
                                className="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-custom-blue sm:text-sm sm:leading-6"
                            />
                        </div>
                    </div>
                    <div>
                        <label htmlFor="dropTime" className="block text-md font-medium leading-6 text-gray-900">
                            Drop Time
                        </label>
                        <div className="mt-2">
                            <input
                                id="dropTime"
                                name="dropTime"
                                type="time"
                                required
                                value={dropTime}
                                onChange={(event) => setDropTime(event.target.value)}
                                className="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-custom-blue sm:text-sm sm:leading-6"
                            />
                        </div>
                    </div>
                    <div>
                        <button
                            type="submit"
                            className="w-1/2  rounded-md bg-light-blue px-3 py-1.5 text-sm font-semibold leading-6 text-white shadow-sm hover:bg-custom-blue focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-custom-blue"
                        >
                            Search for Cars
                        </button>
                    </div>
                </form>
            </div>
        </>




    )
}

export default SplashPage;

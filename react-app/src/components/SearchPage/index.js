
import Car from '../Car';
import { useSelector } from 'react-redux';

const SearchPage = () => {
    const available_cars = useSelector((state) => state.cars);
    return (
        <div>
            <h2>Search Page</h2>
            {available_cars?.data && available_cars?.data.map((car) =>
                <Car data={car} />
            )}
        </div>
    )
}

export default SearchPage;

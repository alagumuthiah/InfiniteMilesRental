import './Car.css';

const Car = () => {
    return (
        <div className="car-container">
            <div className="inline-div car-category-image">
                <h3>Image place holder</h3>
            </div>
            <div className="inline-div main-card-info">
                <h2>Car name</h2>
                <p>Car info</p>
            </div>
            <div className="inline-div cost-info">
                <h3>Cost</h3>
                <button
                    type="submit"
                    className="rounded-md bg-light-blue px-3 py-1.5 text-sm font-semibold leading-6 text-white shadow-sm hover:bg-custom-blue focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-custom-blue"
                >Pay</button>
            </div>
        </div>
    )
}

export default Car;

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
                <button>Pay Now</button>
            </div>
        </div>
    )
}

export default Car;

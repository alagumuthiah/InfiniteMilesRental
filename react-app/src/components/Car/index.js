import './Car.css';

const Car = (props) => {
    return (
        <>
            <div className="container">
                <div className="section-1">
                    <img src="/car_image.jpg" alt="car"></img>
                    <h2>{props.data.supplier}</h2>
                </div>
                <div className="section-2">
                    <h1>{props.data.subcategory} {props.data.category}</h1>
                    <h2>{props.data.name} or similar</h2>
                </div>
                <div className="section-3">
                    <h1>{props.data.price}/day</h1>
                    <button
                        type="submit"
                        className="rounded-md bg-light-blue px-3 py-1.5 text-sm font-semibold leading-6 text-white shadow-sm hover:bg-custom-blue focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-custom-blue"
                    >Pay</button>
                </div>
            </div>
        </>

    )
}

export default Car;

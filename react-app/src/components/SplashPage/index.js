import './SplashPage.css';

const SplashPage = () => {
    return (
        <div className="container">
            <div className="header">
                <h4>Navigate Your Adventure: Where Every Mile Tells a Story!</h4>
            </div>
            <div className="search-bar">
                <input type="text" placeholder="Location"></input>
                <input type="date" placeholder="pickup date"></input>
                <input type="time" placeholder="pickup time"></input>
                <input type="date" placeholder="drop-off date"></input>
                <input type="time" placeholder="drop-off time"></input>
                <button type="submit" className="search-button">Search for Car</button>
            </div>
        </div>



    )
}

export default SplashPage;

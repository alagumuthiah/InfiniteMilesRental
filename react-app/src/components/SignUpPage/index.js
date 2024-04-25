import { useState, useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { useNavigate } from 'react-router-dom';
import { signUpUser } from '../../store/userSlice';
const SignUpPage = () => {
    const [firstName, setFirstName] = useState('');
    const [lastName, setLastName] = useState('');
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [confirmPassword, setConfirmPassword] = useState('');
    const navigate = useNavigate();
    const dispatch = useDispatch();
    const userInfo = useSelector((state) => state.user);

    useEffect(() => {
        if (userInfo?.data) {
            navigate("/");
        } else if (userInfo?.error) {
            alert(userInfo?.error);
        }
    }, [navigate, userInfo]);

    const handleSubmit = (event) => {
        event.preventDefault();
        const payload = {
            firstName,
            lastName,
            email,
            password,
            confirmPassword
        }
        console.log(password);
        if (password === confirmPassword) {
            dispatch(signUpUser(payload));
        } else {
            alert("Passwords don't match, try again");
        }
    }
    return (
        <>
            <div className="sm:mx-auto sm:w-full sm:max-w-sm">
                <h2 className="mt-10 text-center text-2xl font-bold text-gray-900">
                    Sign Up
                </h2>
            </div>
            <div className="mt-10 sm:mx-auto sm:w-full sm:max-w-sm">
                <form className="space-y-4" onSubmit={handleSubmit}>
                    <div className="mt-2 flex items-center justify-between">
                        <label htmlFor="firstname"
                            className="w-1/3 text-md font-medium leading-6 text-gray-900 ">
                            FirstName
                        </label>
                        <input
                            id="firstname"
                            name="firstname"
                            type="text"
                            value={firstName}
                            onChange={(event) => setFirstName(event.target.value)}
                            required
                            className="w-2/3 ml-2 block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm
                            ring-1 ring-inset ring-gray-500
                            focus:ring-2 focus:ring-inset focus:ring-custom-blue sm:text-sm sm:leading-6" />
                    </div>
                    <div className="mt-2 flex items-center justify-between">
                        <label htmlFor="lastname"
                            className="w-1/3 text-md font-medium leading-6 text-gray-900 ">
                            LastName
                        </label>
                        <input
                            id="lastname"
                            name="lastname"
                            type="text"
                            value={lastName}
                            onChange={(event) => setLastName(event.target.value)}
                            required
                            className="w-2/3 ml-2 block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm
                            ring-1 ring-inset ring-gray-500
                            focus:ring-2 focus:ring-inset focus:ring-custom-blue sm:text-sm sm:leading-6" />
                    </div>
                    <div className="mt-2 flex items-center justify-between">
                        <label htmlFor="email"
                            className="w-1/3 text-md font-medium leading-6 text-gray-900 ">
                            Email
                        </label>
                        <input
                            id="email"
                            name="email"
                            type="email"
                            value={email}
                            onChange={(event) => setEmail(event.target.value)}
                            required
                            className="w-2/3 ml-2 block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm
                            ring-1 ring-inset ring-gray-500
                            focus:ring-2 focus:ring-inset focus:ring-custom-blue sm:text-sm sm:leading-6" />
                    </div>
                    <div className="mt-2 flex items-center justify-between">
                        <label htmlFor="password"
                            className="w-1/3 text-md font-medium leading-6 text-gray-900 ">
                            Password
                        </label>
                        <input
                            id="password"
                            name="password"
                            type="password"
                            value={password}
                            onChange={(event) => setPassword(event.target.value)}
                            required
                            className="w-2/3 ml-2 block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm
                            ring-1 ring-inset ring-gray-500
                            focus:ring-2 focus:ring-inset focus:ring-custom-blue sm:text-sm sm:leading-6" />
                    </div>
                    <div className="mt-2 flex items-center justify-between">
                        <label htmlFor="email"
                            className="w-1/3 text-md font-medium leading-6 text-gray-900 ">
                            Confirm Password
                        </label>
                        <input
                            id="confirmpassword"
                            name="confirmpassword"
                            type="password"
                            value={confirmPassword}
                            onChange={(event) => setConfirmPassword(event.target.value)}
                            required
                            className="w-2/3 ml-2 block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm
                            ring-1 ring-inset ring-gray-500
                            focus:ring-2 focus:ring-inset focus:ring-custom-blue sm:text-sm sm:leading-6" />
                    </div>
                    <div>
                        <button
                            type="submit"
                            className="w-1/2  rounded-md bg-light-blue px-3 py-1.5 text-sm font-semibold leading-6 text-white shadow-sm hover:bg-custom-blue focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-custom-blue"
                        >
                            Create an account
                        </button>
                    </div>
                </form >
            </div >
        </>

    )
}

export default SignUpPage;

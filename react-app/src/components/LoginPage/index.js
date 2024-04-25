import { useState, useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { useNavigate } from 'react-router-dom';
import { loginUser } from '../../store/userSlice';

const LoginPage = () => {
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');

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
        event.preventDefault()
        console.log('Submit button clicked')
        const payload = {
            email,
            password
        }
        console.log(payload);
        dispatch(loginUser(payload));
        handleReset();
    }

    const handleReset = () => {
        setEmail('');
        setPassword('');
    }

    return (
        <>
            <div className="sm:mx-auto sm:w-full sm:max-w-sm">
                <h2 className="mt-10 text-center text-2xl font-bold text-gray-900">
                    Login in to your account
                </h2>
            </div>
            <div className="mt-10 sm:mx-auto sm:w-full sm:max-w-sm">
                <form className="space-y-6" onSubmit={handleSubmit}>
                    <div>
                        <label htmlFor="email" className="block text-md font-medium leading-6 text-gray-900">
                            Email address
                        </label>
                        <div className="mt-2">
                            <input
                                id="email"
                                name="email"
                                type="email"
                                autoComplete="email"
                                required
                                value={email}
                                onChange={(event) => setEmail(event.target.value)}
                                className="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-custom-blue sm:text-sm sm:leading-6"
                            />
                        </div>
                    </div>

                    <div>
                        <div>
                            <label htmlFor="password" className="block text-md font-medium leading-6 text-gray-900">
                                Password
                            </label>
                        </div>
                        <div className="mt-2">
                            <input
                                id="password"
                                name="password"
                                type="password"
                                value={password}
                                onChange={(event) => setPassword(event.target.value)}
                                autoComplete="current-password"
                                required
                                className="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-custom-blue sm:text-sm sm:leading-6"
                            />
                        </div>
                    </div>

                    <div>
                        <button
                            type="submit"
                            className="w-1/2  rounded-md bg-light-blue px-3 py-1.5 text-sm font-semibold leading-6 text-white shadow-sm hover:bg-custom-blue focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-custom-blue"
                        >
                            Login
                        </button>

                    </div>
                </form>

                <p className="mt-8 text-center text-sm text-gray-500">
                    Don't have an account?{' '}
                    <a href="/signup" className="font-semibold leading-6 text-dark-blue hover:text-custom-blue">
                        SignUp
                    </a>
                </p>
            </div>
        </>
    )
}

export default LoginPage;

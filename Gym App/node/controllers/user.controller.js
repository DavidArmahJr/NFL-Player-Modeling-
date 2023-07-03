const userService = require('../services/user.service')


module.exports = {
    authenticate,
    getAllUsers,
    register,
    registerGym,
    trackProgress,
    getUserInfo,
    getGymLeaderboards
};


function authenticate(req, res, next) {
    console.log("Authenticate():", req.body);
       userService.authenticate(req.body)
        .then(user => user ? res.json(user) : res.status(400).json({ message: 'Username or password is incorrect' }))
        .catch(err => next(err));
}

function getAllUsers(req, res, next) {
    //  console.log("getAll", req.body);
    userService.getAllUsers()
        .then(users => res.json(users))
        .catch(err => next(err));
}

function register(req, res, next) {

   userService.addUser(req.body)
        .then(() => res.json({}))
        .catch(err => next(err));
}


function registerGym(req, res, next) {
    userService.registerGym(req)
        .then(() => res.json({}))
        .catch(err => next(err));


}

function trackProgress(req, res, next){
    userService.trackProgress(req)
        .then(() => res.json({}))
        .catch(err => next(err));


}
function getUserInfo(req, res, next){
    userService.getUserInfo(req)
        .then(users => res.json(users))
        .catch(err => next(err));


}

function getGymLeaderboards(req, res, next){
    console.log(req);
    userService.getGymLeaderboards(req)
        .then(users => res.json(users))
        .catch(err => next(err));


}

const config = require('../config.json');
const jwt = require('jsonwebtoken');
const bcrypt = require('bcryptjs');
const db = require('../_helpers/database');
const User = db.User;
const Gym = db.Gym;
module.exports = {
    authenticate,
    getAllUsers,
    getById,
    addUser,
    registerGym,
    trackProgress,
    getUserInfo,
    getGymLeaderboards

}

async function authenticate({ username, password }) {
    const user = await User.findOne({ username });
    if (user && bcrypt.compareSync(password, user.hash)) {
        const { hash, ...userWithoutHash } = user.toObject();
        const token = jwt.sign({ sub: user.id, role: user.role }, config.secret);
        return {
            ...userWithoutHash,
            token
        };
    }

}

async function getAllUsers() {
    return await User.find().select('-hash');
}



async function getById(id) {

    return await User.find({_id:id});
}

async function registerGym(req){
    // console.log(req);
    const user = await User.findOne({_id: req.user.sub});





    return await User.updateOne({_id: req.user.sub}, {$push: {gyms: req.body.gymID}});

}

async function addUser(userParam) {

    // validate
    if (await User.findOne({ username: userParam.username })) {
        throw 'Username "' + userParam.username + '" is already taken';
    }
    else  if (await User.findOne({ email: userParam.email })) {
        throw 'Email "' + userParam.email + '" is already taken';
    }

    const user = new User(userParam);

    // hash password
    if (userParam.password) {
        user.hash = bcrypt.hashSync(userParam.password, 10);
    }

    // save user
    await user.save();

}

async function trackProgress(req){
    // console.log(req.body.todaysDate);
    const user = await User.findOne({_id: req.user.sub});
    // console.log(user.username);
    let progress =  req.body.todaysDate + " " + req.body.workoutType + " " + req.body.duration + " " + req.body.poundslost;
   // console.log(req.body);
   //  if ( req.body.gymName !=  )
    return await User.updateOne({_id: req.user.sub}, {$push: {progresses: progress}});
}

async function getUserInfo(req) {
    console.log(req.user.sub);
    console.log(req.body);
    let a = await User.findOne({_id: req.user.sub});
   // let a = await User.find({user: req.user.sub});
    console.log(a.progresses);
    return a.progresses;
}

async function getGymLeaderboards(req){
    console.log(req.query);

    // const users = await User.find({gyms: {$elemMatch:{_id: req.query.gymID}}})
    const users = await User.find({gyms: req.query.gymID})
    console.log(users);
    console.log(users.length);
    if ( users.length > 0) {
        users.forEach((user) => {
            let totalPoundsLost = 0;
            user.progresses.forEach((progress) => {
                totalPoundsLost += parseInt(progress.toString().split(' ')[3]);
            })

            user.totalPoundsLost = totalPoundsLost.toString();
        })
    }


    return users;




}


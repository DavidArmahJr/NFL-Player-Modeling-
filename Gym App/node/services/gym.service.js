const db = require('../_helpers/database');
const mongoose = require("mongoose");
const Gym = db.Gym;
const User = db.User;


module.exports = {
    getGyms,
    addGyms,
    deleteGyms
}


async function getGyms() {

     return await Gym.find().populate({path:'createdBy',select:'username'});
}

async function deleteGyms(id) {
    console.log(id);
      return await Gym.deleteOne({_id:id});
}



async function addGyms(req) {

    let gym = req.body;
    console.log(gym);

    // validate
    if (await Gym.findOne({ name: gym.name  })) {
        throw 'Gym ' + gym.name + ' already exists';
    }
    else if(!req.user.sub){
        throw 'Error with the trainer submitting request. Trainer\'s information is missing. Malformed request.';
    }
    //populate missing fields in the course object
    gym.createdBy = req.user.sub;

    gym = new Gym(gym);

    // save user
    await gym.save();
}

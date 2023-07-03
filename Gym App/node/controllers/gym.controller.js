const gymService = require('../services/gym.service')

module.exports = {
    createGyms,
    getGyms,
    deleteGyms
};


function createGyms(req, res, next) {

    gymService.addGyms(req)
        .then((message) => res.json(message))
        .catch(err => next(err));

}

function getGyms(req,res,next){

    gymService.getGyms(req).then(gyms => {
        res.json(gyms)}).catch(err => next(err));
}




function deleteGyms(req,res,next){
    gymService.deleteGyms(req.params.id).then(gyms => {
        res.json(gyms)}).catch(err => next(err));
}

const mongoose = require('mongoose');
const Schema = mongoose.Schema;




const schema = new Schema({
    name: {type: String, required: true, unique: true},
    createdBy: { type: Schema.Types.ObjectId, ref: 'User' },
    openDate: {type: Date, default: Date.now},
    location: {type: String,default: "Blacksburg"},
    description: {type: String, unique: true}






    // courseNumber: { type: Number, required: true },
    // courseDept: { type: String, required: true },
    // courseDescription: { type: String, required: true, default:"No description set" },
    // createdBy: { type: Schema.Types.ObjectId, ref: 'User' },
    // createdDate: { type: Date, default: Date.now },
    // startDate: { type: Date, default: Date.now },
    // endDate: { type: Date, default: Date.now },
    // latitude: {type: Number, default: 37.2296},
    // longitude: {type: Number, default: 80.4139},
    // location: {type: String, default: "Blacksburg"}



});

// schema.index({courseNumber:1, courseDeptCode:1}, { unique: true });

schema.set('toJSON', { virtuals: true });

module.exports = mongoose.model('Gym', schema);

const mongoose = require('mongoose');
const Schema = mongoose.Schema;

const schema = new Schema({
        username: { type: String, unique: true, required: true },
        email: { type: String, unique: true, required: true },
        hash: { type: String, required: true },
        firstName: { type: String, required: true },
        lastName: { type: String, required: true },
        totalPoundsLost: { type: String, default: '0'},
        role: {type:String, required: true},
        joinedDate: { type: Date, default: Date.now },
        gyms: [{type: Schema.Types.ObjectId, ref: 'Gym' }],
        progresses: [{type: String}]

    }
);

schema.set('toJSON', { virtuals: true });

module.exports = mongoose.model('User', schema);

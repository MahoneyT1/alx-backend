import kue from "kue";

const queue = kue.createQueue()

const jobData = {
    phoneNumber: "08131325356",
    message: "Hello world"
}

const push_notification_code = kue.createQueue()

const job = push_notification_code.create('notification', jobData)
.save((err)=> {
    if (err) {
        console.error(`Notification job failed ${err}`)
    }
    else {
        console.log(`Notification job created: ${job.id}`)
    }
})

push_notification_code.process("complete", (job, done)=> {
    console.log(`Notification job completed ${job.data}`)
    done();
});

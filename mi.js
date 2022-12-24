const miio = require('miio');

miio.device({ address: '192.168.0.101', token: '3a8ff161dd25b4cc332b8afd874b2615' })
  .then(async function (device) {
    console.log('Connected to', device);
    device.power().then(isOn => console.log('Outlet power:', isOn));
    // await device.setPower(true);
    // await device.setPower(false);
    device.destroy();
  }).catch(err => console.error(err));

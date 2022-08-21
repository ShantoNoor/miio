const miio = require('miio');

miio.device({ address: '192.168.0.51', token: '2560f5ab98edbed5a67062108c50bb33' })
  .then(async function (device) {
    console.log('Connected to', device);
    device.power().then(isOn => console.log('Outlet power:', isOn));
    // await device.setPower(true);
    // wait device.setPower(false);
    device.destroy();
  }).catch(err => console.error(err));

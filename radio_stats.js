let stats = {
  listeners: 1000,
  impressions: 5000,
  cpm: 2.5,  // $ за 1000 показов
  tax: 0     // IT Park
};
let revenue = (stats.listeners * stats.impressions * stats.cpm) / 1000000;
console.log(`💰 Доход: $${revenue.toFixed(2)}`);
console.log(`📊 Слушатели: ${stats.listeners}`);
console.log(`🎯 Показы: ${stats.impressions}`);

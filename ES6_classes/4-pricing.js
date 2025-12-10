import Currency from './3-currency.js';

export default class Pricing {
  constructor(amount, currency) {
    this.amount = amount;
    this.currency = currency;
  }

    // Getter and Setter for amount
    get amount() {
        return this._amount;
    }

    set amount(value) {
        if (typeof value !== 'number') {
            throw new TypeError('amount must be a number');
        }
        this._amount = value;
    }
 
    // Getter and Setter for currency
    get currency() {
        return this._currency;
    }

    set currency(value) {
        if (!(value instanceof Currency)) {
        throw new TypeError('currency must be a Currency object');
        }
        this._currency = value;
    }

    displayFullPrice() {
        return `${this._amount} ${this._currency.name} (${this._currency.code})`;
    }

    static convertPrice(amount, conversionRate) {
        return amount * conversionRate;
    }
}

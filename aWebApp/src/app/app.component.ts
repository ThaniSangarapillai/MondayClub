import { Component, OnInit } from '@angular/core';
import { StocksComponent } from './stocks/stocks.component';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent implements OnInit {
  static stocksymbol(stocksymbol: any) {
    throw new Error("Method not implemented.");
  }
  title = 'aWebApp';
  public stocksymbol;

  ngOnInit() : void {
    this.stocksymbol = "MSFT".toString();
  }
}

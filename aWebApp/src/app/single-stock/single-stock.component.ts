import { Component, OnInit } from '@angular/core';
import { HttpService } from '../http.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-single-stock',
  templateUrl: './single-stock.component.html',
  styleUrls: ['./single-stock.component.scss']
})
export class SingleStockComponent implements OnInit {

  searchName: string = '';

  stockname: string = '';

  price = 100.64;

  LPValue = 99.74;

  MTime: string = '4:00PM EDT';

  CValue = -7.5;

  ChangePValue = -0.65;

  VValue = 100000;

  MCValue = 1243245;

  IHValue = 101.64;

  ILValue = 98.89;

  data: object;

  constructor(private _http: HttpService, private router: Router) { }

  ngOnInit(): void {
    this._http.getInfo().subscribe(data => {
      this.stockname = data[0].ticker;
      console.log(data.ticker);
    })
  }

  search(): void {
    this._http.search(this.searchName).subscribe(data => {
      if (data.status !== undefined)
        this.router.navigate(["/singlestock"]);        
    })
  }

}

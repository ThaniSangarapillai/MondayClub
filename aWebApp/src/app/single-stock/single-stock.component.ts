import { Component, OnInit } from '@angular/core';
import { HttpService } from '../http.service';
import { Router } from '@angular/router';
import { Subscription, timer } from 'rxjs';
import { switchMap } from 'rxjs/operators';


@Component({
  selector: 'app-single-stock',
  templateUrl: './single-stock.component.html',
  styleUrls: ['./single-stock.component.scss']
})
export class SingleStockComponent implements OnInit {

  stockname: string = 'Mo vs Thani';

  price = 100.64;

  LPValue = 99.74;

  MTime: string = '4:00PM EDT';

  CValue = -7.5;

  ChangePValue = -0.65;

  VValue = 100000;

  MCValue = 1243245;

  IHValue = 101.64;

  ILValue = 98.89;

  subscription: Subscription;
  newsIndex = [];

  constructor(private _http: HttpService, private router: Router) { }

  ngOnInit(): void {
    this.subscription = timer(0, 10000).pipe(
      switchMap(() => this._http.getnews(this.stockname))
    ).subscribe(result => {
      console.log(result)
      // for (let x in result) {
      //   this.newsIndex.push({
      //     "source": result[x].source,
      //     "title": result[x].title,
      //     "author": result[x].author,
      //     "description": result[x].description,
      //     "url": result[x].url,
      //     "image": result[x].image,
      //     "content": result[x].content,
      //     "sentiment": result[x].sentiment
      //   });
      // }
    });
  }

  search() {
    if (this._http.search(this.stockname))
      this.router.navigate(["/singlestock"]);
  }

  ngOnDestroy() {
    this.subscription.unsubscribe();
  }

}

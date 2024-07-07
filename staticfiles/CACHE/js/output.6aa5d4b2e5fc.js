!function(t,e){"use strict";"function"==typeof define&&define.amd?define(["moment"],e):"object"==typeof module&&module.exports?module.exports=e(require("moment")):e(t.moment)}(this,function(t){"use strict";function e(t){return t>96?t-87:t>64?t-29:t-48}function n(t){var n=0,o=t.split("."),r=o[0],s=o[1]||"",i=1,f=0,a=1;for(45===t.charCodeAt(0)&&(n=1,a=-1),n;n<r.length;n++)f=60*f+e(r.charCodeAt(n));for(n=0;n<s.length;n++)i/=60,f+=e(s.charCodeAt(n))*i;return f*a}function o(t){for(var e=0;e<t.length;e++)t[e]=n(t[e])}function r(t,e){for(var n=0;n<e;n++)t[n]=Math.round((t[n-1]||0)+6e4*t[n]);t[e-1]=1/0}function s(t,e){var n,o=[];for(n=0;n<e.length;n++)o[n]=t[e[n]];return o}function i(t){var e=t.split("|"),n=e[2].split(" "),i=e[3].split(""),f=e[4].split(" ");return o(n),o(i),o(f),r(f,i.length),{name:e[0],abbrs:s(e[1].split(" "),i),offsets:s(n,i),untils:f,population:0|e[5]}}function f(t){t&&this._set(i(t))}function a(t){var e=t.toTimeString(),n=e.match(/\([a-z ]+\)/i);"GMT"===(n=n&&n[0]?(n=n[0].match(/[A-Z]/g))?n.join(""):void 0:(n=e.match(/[A-Z]{3,5}/g))?n[0]:void 0)&&(n=void 0),this.at=+t,this.abbr=n,this.offset=t.getTimezoneOffset()}function u(t){this.zone=t,this.offsetScore=0,this.abbrScore=0}function c(t,e){for(var n,o;o=6e4*((e.at-t.at)/12e4|0);)(n=new a(new Date(t.at+o))).offset===t.offset?t=n:e=n;return t}function h(){var t,e,n,o=(new Date).getFullYear()-2,r=new a(new Date(o,0,1)),s=[r];for(n=1;n<48;n++)(e=new a(new Date(o,n,1))).offset!==r.offset&&(t=c(r,e),s.push(t),s.push(new a(new Date(t.at+6e4)))),r=e;for(n=0;n<4;n++)s.push(new a(new Date(o+n,0,1))),s.push(new a(new Date(o+n,6,1)));return s}function l(t,e){return t.offsetScore!==e.offsetScore?t.offsetScore-e.offsetScore:t.abbrScore!==e.abbrScore?t.abbrScore-e.abbrScore:e.zone.population-t.zone.population}function p(t,e){var n,r;for(o(e),n=0;n<e.length;n++)r=e[n],x[r]=x[r]||{},x[r][t]=!0}function d(t){var e,n,o,r=t.length,s={},i=[];for(e=0;e<r;e++){o=x[t[e].offset]||{};for(n in o)o.hasOwnProperty(n)&&(s[n]=!0)}for(e in s)s.hasOwnProperty(e)&&i.push(D[e]);return i}function m(){try{var t=Intl.DateTimeFormat().resolvedOptions().timeZone;if(t&&t.length>3){var e=D[v(t)];if(e)return e;y("Moment Timezone found "+t+" from the Intl api, but did not have that data loaded.")}}catch(t){}var n,o,r,s=h(),i=s.length,f=d(s),a=[];for(o=0;o<f.length;o++){for(n=new u(b(f[o]),i),r=0;r<i;r++)n.scoreOffsetAt(s[r]);a.push(n)}return a.sort(l),a.length>0?a[0].zone.name:void 0}function v(t){return(t||"").toLowerCase().replace(/\//g,"_")}function z(t){var e,n,o,r;for("string"==typeof t&&(t=[t]),e=0;e<t.length;e++)r=v(n=(o=t[e].split("|"))[0]),M[r]=t[e],D[r]=n,p(r,o[2].split(" "))}function b(t,e){t=v(t);var n,o=M[t];return o instanceof f?o:"string"==typeof o?(o=new f(o),M[t]=o,o):j[t]&&e!==b&&(n=b(j[t],b))?((o=M[t]=new f)._set(n),o.name=D[t],o):null}function g(t){var e,n,o,r;for("string"==typeof t&&(t=[t]),e=0;e<t.length;e++)o=v((n=t[e].split("|"))[0]),r=v(n[1]),j[o]=r,D[o]=n[0],j[r]=o,D[r]=n[1]}function _(t){return _.didShowError||(_.didShowError=!0,y("moment.tz.zoneExists('"+t+"') has been deprecated in favor of !moment.tz.zone('"+t+"')")),!!b(t)}function w(t){var e="X"===t._f||"x"===t._f;return!(!t._a||void 0!==t._tzm||e)}function y(t){"undefined"!=typeof console&&"function"==typeof console.error&&console.error(t)}function S(e){var n=Array.prototype.slice.call(arguments,0,-1),o=arguments[arguments.length-1],r=b(o),s=t.utc.apply(null,n);return r&&!t.isMoment(e)&&w(s)&&s.add(r.parse(s),"minutes"),s.tz(o),s}function O(t){return function(){return this._z?this._z.abbr(this):t.call(this)}}var A,M={},j={},D={},x={},T=t.version.split("."),Z=+T[0],F=+T[1];(Z<2||2===Z&&F<6)&&y("Moment Timezone requires Moment.js >= 2.6.0. You are using Moment.js "+t.version+". See momentjs.com"),f.prototype={_set:function(t){this.name=t.name,this.abbrs=t.abbrs,this.untils=t.untils,this.offsets=t.offsets,this.population=t.population},_index:function(t){var e,n=+t,o=this.untils;for(e=0;e<o.length;e++)if(n<o[e])return e},parse:function(t){var e,n,o,r,s=+t,i=this.offsets,f=this.untils,a=f.length-1;for(r=0;r<a;r++)if(e=i[r],n=i[r+1],o=i[r?r-1:r],e<n&&S.moveAmbiguousForward?e=n:e>o&&S.moveInvalidForward&&(e=o),s<f[r]-6e4*e)return i[r];return i[a]},abbr:function(t){return this.abbrs[this._index(t)]},offset:function(t){return y("zone.offset has been deprecated in favor of zone.utcOffset"),this.offsets[this._index(t)]},utcOffset:function(t){return this.offsets[this._index(t)]}},u.prototype.scoreOffsetAt=function(t){this.offsetScore+=Math.abs(this.zone.utcOffset(t.at)-t.offset),this.zone.abbr(t.at).replace(/[^A-Z]/g,"")!==t.abbr&&this.abbrScore++},S.version="0.5.14",S.dataVersion="",S._zones=M,S._links=j,S._names=D,S.add=z,S.link=g,S.load=function(t){z(t.zones),g(t.links),S.dataVersion=t.version},S.zone=b,S.zoneExists=_,S.guess=function(t){return A&&!t||(A=m()),A},S.names=function(){var t,e=[];for(t in D)D.hasOwnProperty(t)&&(M[t]||M[j[t]])&&D[t]&&e.push(D[t]);return e.sort()},S.Zone=f,S.unpack=i,S.unpackBase60=n,S.needsOffset=w,S.moveInvalidForward=!0,S.moveAmbiguousForward=!1;var k=t.fn;t.tz=S,t.defaultZone=null,t.updateOffset=function(e,n){var o,r=t.defaultZone;void 0===e._z&&(r&&w(e)&&!e._isUTC&&(e._d=t.utc(e._a)._d,e.utc().add(r.parse(e),"minutes")),e._z=r),e._z&&(o=e._z.utcOffset(e),Math.abs(o)<16&&(o/=60),void 0!==e.utcOffset?e.utcOffset(-o,n):e.zone(o,n))},k.tz=function(e,n){return e?(this._z=b(e),this._z?t.updateOffset(this,n):y("Moment Timezone has no data for "+e+". See http://momentjs.com/timezone/docs/#/data-loading/."),this):this._z?this._z.name:void 0},k.zoneName=O(k.zoneName),k.zoneAbbr=O(k.zoneAbbr),k.utc=function(t){return function(){return this._z=null,t.apply(this,arguments)}}(k.utc),t.tz.setDefault=function(e){return(Z<2||2===Z&&F<9)&&y("Moment Timezone setDefault() requires Moment.js >= 2.9.0. You are using Moment.js "+t.version+"."),t.defaultZone=e?b(e):null,t};var C=t.momentProperties;return"[object Array]"===Object.prototype.toString.call(C)?(C.push("_z"),C.push("_a")):C&&(C._z=null),t});;
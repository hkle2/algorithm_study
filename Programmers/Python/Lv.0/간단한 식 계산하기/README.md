
  <h1><a href="https://school.programmers.co.kr/learn/courses/30/lessons/181865">간단한 식 계산하기</a></h1><p>문자열 <code>binomial</code>이 매개변수로 주어집니다. <code>binomial</code>은 "<code>a</code> <code>op</code> <code>b</code>" 형태의 이항식이고 <code>a</code>와 <code>b</code>는 음이 아닌 정수, <code>op</code>는 '+', '-', '*' 중 하나입니다. 주어진 식을 계산한 정수를 return 하는 solution 함수를 작성해 주세요.</p>



<h3>제한사항</h3>

<ul>
<li>0 ≤ <code>a</code>, <code>b</code> ≤ 40,000</li>
<li>0을 제외하고 <code>a</code>, <code>b</code>는 0으로 시작하지 않습니다.</li>
</ul>



<h3>입출력 예</h3>
<table class="table">
        <thead><tr>
<th>binomial</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td>"43 + 12"</td>
<td>55</td>
</tr>
<tr>
<td>"0 - 7777"</td>
<td>-7777</td>
</tr>
<tr>
<td>"40000 * 40000"</td>
<td>1600000000</td>
</tr>
</tbody>
      </table>


<h3>입출력 예 설명</h3>

<p>입출력 예 #1</p>

<ul>
<li>예제 1번의 <code>binomial</code>은 "43 + 12"로 이 식을 계산한 결과인 43 + 12 = 55를 return 합니다.</li>
</ul>

<p>입출력 예 #2</p>

<ul>
<li>예제 2번의 <code>binomial</code>은 "0 - 7777"로 이 식을 계산한 결과인 0 - 7777 = -7777을 return 합니다.</li>
</ul>

<p>입출력 예 #3</p>

<ul>
<li>예제 3번의 <code>binomial</code>은 "40000 * 40000"으로 이 식을 계산한 결과인 40000 × 40000 = 1600000000을 return 합니다.</li>
</ul>

  
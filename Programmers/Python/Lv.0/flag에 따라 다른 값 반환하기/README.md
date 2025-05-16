
  <h1><a href="https://school.programmers.co.kr/learn/courses/30/lessons/181933">flag에 따라 다른 값 반환하기</a></h1><p>두 정수 <code>a</code>, <code>b</code>와 boolean 변수 <code>flag</code>가 매개변수로 주어질 때, <code>flag</code>가 true면 <code>a</code> + <code>b</code>를 false면 <code>a</code> - <code>b</code>를 return 하는 solution 함수를 작성해 주세요.</p>



<h3>제한사항</h3>

<ul>
<li>-1,000 ≤ <code>a</code>, <code>b</code> ≤ 1,000</li>
</ul>



<h3>입출력 예</h3>
<table class="table">
        <thead><tr>
<th>a</th>
<th>b</th>
<th>flag</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td>-4</td>
<td>7</td>
<td>true</td>
<td>3</td>
</tr>
<tr>
<td>-4</td>
<td>7</td>
<td>false</td>
<td>-11</td>
</tr>
</tbody>
      </table>


<h3>입출력 예</h3>

<p>입출력 예 #1</p>

<ul>
<li>예제 1번에서 <code>flag</code>가 true이므로 <code>a</code> + <code>b</code> = (-4) + 7 = 3을 return 합니다.</li>
</ul>

<p>입출력 예 #2</p>

<ul>
<li>예제 2번에서 <code>flag</code>가 false이므로 <code>a</code> - <code>b</code> = (-4) - 7 = -11을 return 합니다.</li>
</ul>

  
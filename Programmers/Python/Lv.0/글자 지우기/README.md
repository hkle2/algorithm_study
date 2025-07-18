
  <h1><a href="https://school.programmers.co.kr/learn/courses/30/lessons/181900">글자 지우기</a></h1><p>문자열 <code>my_string</code>과 정수 배열 <code>indices</code>가 주어질 때, <code>my_string</code>에서 <code>indices</code>의 원소에 해당하는 인덱스의 글자를 지우고 이어 붙인 문자열을 return 하는 solution 함수를 작성해 주세요.</p>



<h3>제한사항</h3>

<ul>
<li>1 ≤ <code>indices</code>의 길이 &lt; <code>my_string</code>의 길이 ≤ 100</li>
<li><code>my_string</code>은 영소문자로만 이루어져 있습니다</li>
<li>0 ≤ <code>indices</code>의 원소 &lt; <code>my_string</code>의 길이</li>
<li><code>indices</code>의 원소는 모두 서로 다릅니다.</li>
</ul>



<h3>입출력 예</h3>
<table class="table">
        <thead><tr>
<th>my_string</th>
<th>indices</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td>"apporoograpemmemprs"</td>
<td>[1, 16, 6, 15, 0, 10, 11, 3]</td>
<td>"programmers"</td>
</tr>
</tbody>
      </table>


<h3>입출력 예 설명</h3>

<p>입출력 예 #1</p>

<ul>
<li>예제 1번의 <code>my_string</code>의 인덱스가 잘 보이도록 표를 만들면 다음과 같습니다.</li>
</ul>
<table class="table">
        <thead><tr>
<th>index</th>
<th>0</th>
<th>1</th>
<th>2</th>
<th>3</th>
<th>4</th>
<th>5</th>
<th>6</th>
<th>7</th>
<th>8</th>
<th>9</th>
<th>10</th>
<th>11</th>
<th>12</th>
<th>13</th>
<th>14</th>
<th>15</th>
<th>16</th>
<th>17</th>
<th>18</th>
</tr>
</thead>
        <tbody><tr>
<td>my_string</td>
<td>a</td>
<td>p</td>
<td>p</td>
<td>o</td>
<td>r</td>
<td>o</td>
<td>o</td>
<td>g</td>
<td>r</td>
<td>a</td>
<td>p</td>
<td>e</td>
<td>m</td>
<td>m</td>
<td>e</td>
<td>m</td>
<td>p</td>
<td>r</td>
<td>s</td>
</tr>
</tbody>
      </table><div class="highlight"><pre class="codehilite"><code>`indices`에 있는 인덱스의 글자들을 지우고 이어붙이면 "programmers"가 되므로 이를 return 합니다.
</code></pre></div>
  
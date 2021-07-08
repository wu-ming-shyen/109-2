package com.example.afinal;

import androidx.appcompat.app.AlertDialog;
import androidx.core.content.ContextCompat;
import androidx.appcompat.app.AppCompatActivity;

import android.view.View;
import android.os.Bundle;
import android.widget.Toast;
import android.view.Gravity;
import android.widget.Button;
import android.content.Intent;
import android.graphics.Color;
import android.widget.TextView;
import android.content.Context;
import android.widget.ImageButton;
import android.widget.LinearLayout;
import android.content.DialogInterface;

import java.util.Set;
import java.util.List;
import java.util.Timer;
import java.util.HashSet;
import java.util.ArrayList;
import java.util.TimerTask;

public class MainActivity extends AppCompatActivity implements View.OnClickListener, View.OnLongClickListener {

    Timer timer;
    Double time = 0.0;
    Set<Integer> bomb;
    TextView timerText;
    TimerTask timerTask;
    LinearLayout buttons;
    LinearLayout textviews;
    int[][] map = new int[10][10];
    List<Integer> flag = new ArrayList<Integer>();
    List<Button> buttonList = new ArrayList<Button>();

    public void reseMap(){
        for (int i = 0; i < 10; i++) {
            for (int j = 0; j < 10; j++) {
                map[i][j] = 0;
            }
        }
    }
    private Set<Integer> getRandom() {
        Set<Integer> set = new HashSet<Integer>();
        while (set.size() != 10) {
            int random = (int) (Math.random() * 100);
            set.add(random);
        }
        return set;
    }
    private void setData() {
        bomb = getRandom();
        for (Integer integer : bomb) {
            int row = integer / 10;// 98
            int col = integer % 10;
            map[row][col] = -1;
        }
        for (int i = 0; i < 10; i++) {
            for (int j = 0; j < 10; j++) {
                if (map[i][j] == -1) {
                    continue;
                }
                else {
                    int sum = 0;
                    if((i != 0 && j != 0) && (map[i - 1][j - 1] == -1)){sum++;}
                    if((j != 0) && (map[i][j - 1] == -1)){sum++;}
                    if((j != 0 && i != 9) && (map[i + 1][j - 1] == -1)){sum++;}
                    if((i != 0) && (map[i - 1][j] == -1)){sum++;}
                    if((i != 9) && (map[i + 1][j] == -1)){sum++;}
                    if((j != 9 && i != 0) && (map[i - 1][j + 1] == -1)){sum++;}
                    if((j != 9) && (map[i][j + 1] == -1)){sum++;}
                    if((j != 9 && i != 9) && (map[i + 1][j + 1] == -1)){sum++;}
                    map[i][j] = sum;
                }
            }
        }
        for (int i = 0; i < 10; i++) {
            for (int j = 0; j < 10; j++) {
                System.out.print(map[i][j] + " ");
            }
            System.out.println();
        }
    }
    private void setView() {
        int width = getResources().getDisplayMetrics().widthPixels / 10;
        LinearLayout.LayoutParams params = new LinearLayout.LayoutParams(width, width);
        for (int i = 0; i < 10; i++) {
            LinearLayout txv = new LinearLayout(this);
            txv.setOrientation(LinearLayout.HORIZONTAL);
            LinearLayout btns = new LinearLayout(this);
            btns.setOrientation(LinearLayout.HORIZONTAL);
            for (int j = 0; j < 10; j++) {
                TextView tv = new TextView(this);
                //tv.setBackgroundResource(R.drawable.textview_bg);
                tv.setLayoutParams(params);
                tv.setGravity(Gravity.CENTER);
                if (map[i][j] == -1)
                    tv.setText("*");
                else if (map[i][j] != 0)
                    tv.setText(map[i][j] + "");
                txv.addView(tv);
                Button btn = new Button(this);
                //btn.setBackgroundResource(R.drawable.button);
                btn.setLayoutParams(params);
                btn.setTag(i * 10 + j);
                btn.setOnClickListener(this);
                btn.setOnLongClickListener(this);
                buttonList.add(btn);
                btns.addView(btn);
            }
            textviews.addView(txv);
            buttons.addView(btns);
        }
    }
    private void hide(int i, int j) {
        int position = i * 10 + j;
        buttonList.get(position).setVisibility(View.INVISIBLE);
    }
    boolean recursive(int row, int col) {
        int position = row * 10 + col;
        if (buttonList.get(position).getVisibility() == View.INVISIBLE)
            return false;
        else
            return true;
    }
    public void showNull(int i, int j) {
        buttonList.get(i * 10 + j).setVisibility(View.INVISIBLE);
        if (i != 0 && j != 0) {
            if (map[i - 1][j - 1] == 0) {
                if (recursive(i - 1, j - 1))
                    showNull(i - 1, j - 1);
            } else {
                hide(i - 1, j - 1);
            }
        }
        if (j != 0) {
            if (map[i][j - 1] == 0) {
                if (recursive(i, j - 1))
                    showNull(i, j - 1);
            } else {
                hide(i, j - 1);
            }
        }
        if (j != 0 && i != 9) {
            if (map[i + 1][j - 1] == 0) {
                if (recursive(i + 1, j - 1))
                    showNull(i + 1, j - 1);
            } else {
                hide(i + 1, j - 1);
            }
        }
        if (i != 0) {
            if (map[i - 1][j] == 0) {
                if (recursive(i - 1, j))
                    showNull(i - 1, j);
            } else {
                hide(i - 1, j);
            }
        }
        if (i != 9) {
            if (map[i + 1][j] == 0) {
                if (recursive(i + 1, j))
                    showNull(i + 1, j);
            } else {
                hide(i + 1, j);
            }
        }
        if (j != 9 && i != 0) {
            if (map[i - 1][j + 1] == 0) {
                if (recursive(i - 1, j + 1))
                    showNull(i - 1, j + 1);
            } else {
                hide(i - 1, j + 1);
            }
        }
        if (j != 9) {
            if (map[i][j + 1] == 0) {
                if (recursive(i, j + 1))
                    showNull(i, j + 1);
            } else {
                hide(i, j + 1);
            }
        }
        if (j != 9 && i != 9) {
            if (map[i + 1][j + 1] == 0) {
                if (recursive(i + 1, j + 1))
                    showNull(i + 1, j + 1);
            } else {
                hide(i + 1, j + 1);
            }
        }
    }
    private boolean gameOver(int row, int col) {
        ImageButton resultButton = (ImageButton)findViewById(R.id.resultButton);
        if (map[row][col] == -1) {
            Toast.makeText(this, "Game Over!", Toast.LENGTH_SHORT).show();
            for (int i = 0; i < buttonList.size(); i++) {
                buttonList.get(i).setVisibility(View.INVISIBLE);
            }
            resultButton.setImageResource(R.drawable.lose);
            timerTask.cancel();
            return true;
        }
        return false;
    }
    public boolean gameWin() {
        int sum = 0;
        ImageButton resultButton = (ImageButton)findViewById(R.id.resultButton);
        for (int i = 0; i < buttonList.size(); i++) {
            if (buttonList.get(i).getVisibility() == View.INVISIBLE) {
                sum++;
            }
        }
        if (sum == 90) {
            resultButton.setImageResource(R.drawable.win);
            timerTask.cancel();
            return true;
        }
        return false;
    }
    private String formatTime(int seconds) {
        return String.format("%02d",seconds);
    }
    private String getTimerText() {
        int rounded = (int) Math.round(time);

        int seconds = ((rounded % 86400) % 3600);

        return formatTime(seconds);
    }
    private void startTimer() {
        timerTask = new TimerTask()
        {
            @Override
            public void run()
            {
                runOnUiThread(new Runnable()
                {
                    @Override
                    public void run()
                    {
                        time++;
                        timerText.setText(getTimerText());
                    }
                });
            }

        };
        timer.scheduleAtFixedRate(timerTask, 0 ,1000);
    }


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        textviews = (LinearLayout) findViewById(R.id.textviews);
        buttons = (LinearLayout) findViewById(R.id.buttons);
        timerText = (TextView) findViewById(R.id.timerText);
        timer = new Timer();
        startTimer();
        reseMap();
        setData();
        setView();
    }

    @Override
    public void onClick(View view) {
        int id = (Integer) view.getTag();
        int row = id / 10;
        int col = id % 10;
        view.setVisibility(View.INVISIBLE);
        gameOver(row, col);
        if (map[row][col] == 0) {
            showNull(row, col);
        }
        if (gameWin()) {
            Toast.makeText(this, "Game Win!", Toast.LENGTH_SHORT).show();
        }
    }
    @Override
    public boolean onLongClick(View view) {
        Button btn = (Button) view;
        TextView flagNum = (TextView)findViewById(R.id.flagNum);
        int tag = (Integer) view.getTag();
        if (flag.contains(tag)) {
            btn.setText("");
            flag.remove((Integer) tag);
        }
        else {
            if (flag.size() != 10) {
                flag.add(tag);
                btn.setText("☢" + flag.size());
                btn.setTextColor(Color.RED);
            } else {
                Toast.makeText(this, "No Flag!", Toast.LENGTH_SHORT).show();
            }
        }
        flagNum.setText(""+(10-flag.size()));
        return true;
    }

    public void newGame(View view) {
        Intent intent = getIntent();
        finish();
        startActivity(intent);
    }
}
/*
參考資料:
https://github.com/codeWithCal/Timer/blob/master/app/src/main/java/codewithcal/au/timer/MainActivity.java
https://codertw.com/android-%E9%96%8B%E7%99%BC/342543/
 */